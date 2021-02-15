from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def homepage(request):
    return render(request, "accounts/base.html")


def logout_request(request):
    logout(request)
    messages.success(request, "successfully logged out!")
    return redirect("homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in user")
                return redirect("homepage")
            else:
                messages.error(request, "incorrect username or password")
        else:
            messages.error(request, "incorrect username or password")
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def index(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successfull")
            return redirect("homepage")
        messages.error(request, "Unsuccessfull login attempt.!")
    else:
        messages.error(request, "Registration Unsuccessfull")
    form = UserCreationForm()
    return render(request, "accounts/index.html", {"form": form})

