from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
    text = models.TextField(null = True)
    complete = models.BooleanField(null = True)
    
    def __str__(self):
        return self.text
    
    