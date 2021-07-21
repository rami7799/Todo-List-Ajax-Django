from django.shortcuts import redirect, render
from .models import Todos
from django.http import JsonResponse , HttpResponse
from django.template.loader import render_to_string 
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request , "home.html")

def login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request , username=username , password=password)
    if user is not None:
        login(user)
        return redirect("/")
    return render(request , "login.html")


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
