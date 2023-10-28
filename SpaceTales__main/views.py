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
