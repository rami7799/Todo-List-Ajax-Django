from django.urls import path
from .views import *


urlpatterns = [
    path('todo-list' , todo_list , name="todo-list"),
    path('' , home , name="home"),
    path("add-todo" , add_todo , name="add_todo"),    
]