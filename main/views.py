from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from joblib import load
import os
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import Item, ToDoList
from .forms import CreateNewList

file_path = os.path.abspath('./KSD/savedModels/model.joblib')
model = load(file_path)

def index(request,id):
    ls = ToDoList.objects.get(id=id)
    return render(request,"crud/list.html", {"ls" : ls})

def home(request):
    current_year = datetime.date.today().year
    return render(request,"home.html",{'date' : current_year})

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        from_email = request.POST["email"]
        phone = request.POST["phone"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        
        html_message = f"""
            <html>
                <head></head>
                <body>
                    <p>Hello Team,</p>
                    <p></p>
                    <p>{message}</p>
                    <p></p>
                    <p>Best Regards,<br>
                        {name}<br>
                        {phone}
                    </p>
                </body>
            </html>
        """
        try:
            send_mail(subject,
                      '', #message
                      from_email,
                      [settings.EMAIL_HOST_USER], #to_email
                      html_message= html_message)
            messages.success(request, "Your message has been sent successfully!")
            return render(request, "contactus.html", {'message' : True})
        except Exception as e:
            messages.error(request, f'Error sending email: {str(e)}')
            return render(request, "contactus.html", {'message' : False})
    return render(request, "contactus.html")

def about(request):
    return render(request, "about.html")

def analyze(request):
    if request.method == "POST":
        gravity = float(request.POST["gravity"])
        ph = float(request.POST["ph"])
        osmolality = float(request.POST["osmolality"])
        conductivity = float(request.POST["conductivity"])
        urea = float(request.POST["urea"])
        calcium = float(request.POST["calcium"])
        y_predict = model.predict([[gravity,ph,osmolality,conductivity,urea,calcium]])
        # print(y_predict)
        if y_predict[0] == 1:
            y_predict = "Detected"
        elif y_predict[0] == 0:
            y_predict = "No Detection"
        return render(request, "analyzeModel.html", {'result' : y_predict})
    return render(request, "analyzeModel.html")
    

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            reqName = form.cleaned_data["name"]
            createRecord = ToDoList(name=reqName)
            createRecord.save()
        return HttpResponseRedirect("%i" %createRecord.id)
    else:
        form = CreateNewList()
    return render(request, "crud/create.html", {"form" : form})