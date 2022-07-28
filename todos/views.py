from django.shortcuts import redirect, render
from .models import Todos
from django.http import JsonResponse , HttpResponse
from django.template.loader import render_to_string 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm



@login_required(login_url="/login")
def home(request):
    return render(request , "home.html")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm(request.POST or None)
    return render(request , "login.html" , {"form" : form})

def register_page(request):
    return render(request , "register.html")

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re-password")
        if password == re_password:
            user = User.objects.filter(username=username).exists()
            if user:
                return HttpResponse("this username already exists !")
            else:
                User.objects.create_user(username=username , password=password , email=email)
            return redirect("/")
        else:
            return HttpResponse("invalid")

def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        login_form = LoginForm(request.POST or None)
        if login_form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username)
            print(password)
            # username = login_form.cleaned_data.get('username')
            # password = login_form.cleaned_data.get('password')
            user = authenticate(request , username=username , password=password)
            # print(user)
            if user is not None:
                login(request , user)
                return redirect("/")
            else:
                return HttpResponse("invalid1")
        return HttpResponse("invalid")



@login_required(login_url="/login")
def add_todo(request):
    if request.method == "POST":
        todo = request.POST.get("todo")
        print(todo)
        Todos.objects.create(title = todo , user_id=request.user.id)
        return HttpResponse("good")


@login_required(login_url="/login")
def delete_todo(request):
    id = request.GET["id"]
    print(id)
    todo = Todos.objects.get(id=id , user_id=request.user.id)
    todo.delete()
    return HttpResponse("task deleted")


@login_required(login_url="/login")
def update_todo(request):
    id = request.GET["id"]
    print(id)
    todo = Todos.objects.get(id=id , user_id=request.user.id)
    todo.completed = True
    todo.save()
    return HttpResponse("task updated")

def log_out(request):
    logout(request)
    return redirect("/login")
