from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserManager
from .models import *


# Create your views here.


def First_page(request):
    return render(request, template_name='PodCast/First_page.html')


def home(request):
    return render(request, template_name='PodCast/home.html')


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('pas')
            pas_confirm = form.cleaned_data.get('pas-confirm')
            user = authenticate(emai=email, username=username, pas=password, pas_confirm=pas_confirm)

        return redirect('login')
    return render(request, 'PodCast/signup.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        pas = request.POST.get('pas')
        my_user = User.objects.create_user(username, pas)
        my_user.save()

        return redirect('userPage')
    return render(request, template_name='PodCast/login.html')


def userPage(request):
    return render(request, template_name='PodCast/user_page.html')


def ArtistPage(request):
    return render(request, template_name='PodCast/ArtistPage.html')


def Episode(request):
    return render(request, template_name='PodCast/Episode.html')
