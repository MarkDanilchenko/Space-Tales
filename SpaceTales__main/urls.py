from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    # films
    path("films/", views.films__list, name="films__list"),
    re_path(r'films/(?P<title>[\w\s]+)/$', views.films__details, name='films__details'),
    # heroes
    # planets
    # spaceships
]
