from django.shortcuts import render
from .models import Todos
from django.http import JsonResponse , HttpResponse


def home(request):

    return render(request , "home.html")

def todo_list(request):
    todos = Todos.objects.order_by("-id")
    todos = todos.values()

    return JsonResponse({'data' : list(todos)})

def add_todo(request):
    if request.method == "POST":
        todo = request.POST.get("todo")
        print(todo)
        Todos.objects.create(title = todo)
        return HttpResponse("good")
         
