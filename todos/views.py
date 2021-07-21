from django.shortcuts import redirect, render
from .models import Todos
from django.http import JsonResponse , HttpResponse
from django.template.loader import render_to_string 
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url="/login")
def home(request):
    return render(request , "home.html")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request , "login.html")

def register_page(request):
    return render(request , "register.html")

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re-password")
        if password == re_password:
            User.objects.create(username=username , email=email , password=password)
            return redirect("/")
        else:
            return HttpResponse("invalid")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect("/")
        else:
            return redirect("/hfgh")


@login_required(login_url="/login")
def todo_list(request):
    todos = Todos.objects.order_by("-id")
    todos = render_to_string("ajax/todo-list.html" , {"todos" : todos})
    return JsonResponse({'data' : todos})


@login_required(login_url="/login")
def add_todo(request):
    if request.method == "POST":
        todo = request.POST.get("todo")
        print(todo)
        Todos.objects.create(title = todo)
        return HttpResponse("good")


@login_required(login_url="/login")
def delete_todo(request):
    id = request.GET["id"]
    print(id)
    todo = Todos.objects.get(id=id)
    todo.delete()
    return HttpResponse("task deleted")


@login_required(login_url="/login")
def update_todo(request):
    id = request.GET["id"]
    print(id)
    todo = Todos.objects.get(id=id)
    todo.completed = True
    todo.save()
    return HttpResponse("task updated")
