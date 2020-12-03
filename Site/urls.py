from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("Team/", views.team, name="team_page"),
    path("Project/", views.project, name="project_page"),
    path("Contact/", views.contact, name="contact_page"),
    path("About/", views.about, name="about_page"),
]