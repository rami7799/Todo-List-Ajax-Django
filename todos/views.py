from django.shortcuts import render
from .models import Todos
from django.http import JsonResponse , HttpResponse
from django.template.loader import render_to_string 



def home(request):
    return render(request , "home.html")

def todo_list(request):
    todos = Todos.objects.order_by("-id")
    todos = render_to_string("ajax/todo-list.html" , {"todos" : todos})
    return JsonResponse({'data' : todos})

def add_todo(request):
    if request.method == "POST":
        todo = request.POST.get("todo")
        print(todo)
        Todos.objects.create(title = todo)
        return HttpResponse("good")
         
def delete_todo(request):
    id = request.GET["id"]
    print(id)
    todo = Todos.objects.get(id=id)
    todo.delete()
    return HttpResponse("task deleted")


def update_todo(request):
    id = request.GET["id"]
    print(id)
    todo = Todos.objects.get(id=id)
    todo.completed = True
    todo.save()
    return HttpResponse("task updated")
