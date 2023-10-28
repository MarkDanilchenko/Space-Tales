import requests
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . import forms


# user registration
# user registration
# user registration
def registration(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data("username")
            password = form.cleaned_data("password1")
            userLogIn = authenticate(username=username, password=password)
            login(request, userLogIn)
            return redirect("/")
    else:
        form = forms.UserForm()
    return render(request, "registration.html", {"form": form})


# root URL
rootURL = "https://swapi.dev/api/"


# films functions
# films functions
# films functions
def films__list(request):
    url = rootURL + "films/"
    response = requests.get(url)
    data = response.json()
    return render(request, "films__list.html", {"data": data})


def films__details(request, title):
    url = rootURL + "films/" + "?search=" + title
    response = requests.get(url)
    data = (response.json()).get("results")[0]
    return render(request, "films__details.html", {"data": data})


# heroes functions
# heroes functions
# heroes functions
def heroes__list(request):
    url = rootURL + "people/"
    response = requests.get(url)
    data = response.json()
    heroes_count = len(data.get('results'))
    return render(request, "heroes__list.html", {"data": data, "heroes_count": heroes_count})


def heroes__details(request, name):
    url = rootURL + "people/" + "?search=" + name
    response = requests.get(url)
    data = (response.json()).get("results")[0]
    return render(request, "heroes__details.html", {"data": data})


# planets functions
# planets functions
# planets functions
def planets__list(request):
    url = rootURL + "planets/"
    response = requests.get(url)
    data = response.json()
    planets_count = len(data.get('results'))
    return render(request, "planets__list.html", {"data": data, "planets_count": planets_count})


def planets__details(request, name):
    url = rootURL + "planets/" + "?search=" + name
    response = requests.get(url)
    data = (response.json()).get("results")[0]
    return render(request, "planets__details.html", {"data": data})


# spaceships functions
# spaceships functions
# spaceships functions
def spaceships__list(request):
    url = rootURL + "starships/"
    response = requests.get(url)
    data = response.json()
    spaceships_count = len(data.get('results'))
    return render(request, "spaceships__list.html", {"data": data, "spaceships_count": spaceships_count})


def spaceships__details(request, model):
    url = rootURL + "starships/" + "?search=" + model
    response = requests.get(url)
    data = (response.json()).get("results")[0]
    return render(request, "spaceships__details.html", {"data": data})
