from django.urls import path
from . import views


urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("", views.home,  name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path('analyze',views.analyze, name="analyze"),
    path("create", views.create, name="create"),
]