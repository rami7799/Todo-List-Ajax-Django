from django.urls import path
from .views import *


urlpatterns = [
    path('' , home , name="home"),    
    path("login" , login_page , name="login-page"),
    path('register' , register_page , name="register-page"),
    path("register-user" , register_user  , name="register-user"),
    path('login-user' , login_user , name="login-user"),
    path('todo-list' , todo_list , name="todo-list"),
    path("add-todo" , add_todo , name="add_todo"),    
    path("delete-todo" , delete_todo , name="delete-todo"),
    path('update-todo' , update_todo , name="update-todo"),
]