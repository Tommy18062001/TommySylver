from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="todo"),
    path("add_todo/", views.add_todo),
    path("deleted/<int:todo_id>", views.deleted),
]

