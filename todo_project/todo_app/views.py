from django.shortcuts import render

from django.views.generic import ListView
from .models import *
# Create your views here.

class ListListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todolist_list.html"