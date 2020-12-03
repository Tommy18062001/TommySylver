from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect

from django.http import HttpResponse
# Create your views here.


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, "ToDoApp/index.html", {
        "todo_items": todo_items
       })


@ csrf_exempt
def add_todo(request):
    # use request.POST to get it
    content = request.POST["content"]
    current_date = timezone.now()

    created_obj = Todo.objects.create(text=content, added_date=current_date)
    length_of_todos = Todo.objects.all().count()

    return HttpResponseRedirect("/ToDoApp")


"""after finishing this part, we need to take the date we got back to the home page"""


@ csrf_exempt
def deleted(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/ToDoApp")


