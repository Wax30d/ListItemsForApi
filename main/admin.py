from django.contrib import admin
from main.models import ToDoItem, ToDoList

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
