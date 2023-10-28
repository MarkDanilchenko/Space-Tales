from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    # films
    path("films/", views.films__list, name="films__list"),
    re_path(r"films/(?P<title>.+)/$", views.films__details, name="films__details"),
    # heroes
    path("heroes/", views.heroes__list, name="heroes__list"),
    re_path(
        r"heroes/(?P<name>.+)/$", views.heroes__details, name="heroes__details"
    ),
    # planets
    path("planets/", views.planets__list, name="planets__list"),
    re_path(
        r"planets/(?P<name>.+)/$", views.planets__details, name="planets__details"
    ),
    # spaceships
    path("spaceships/", views.spaceships__list, name="spaceships__list"),
    re_path(
        r"spaceships/(?P<model>.+)/$",
        views.spaceships__details,
        name="spaceships__details",
    ),
]
