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
    Home = home.objects.all()
    context = {
        'home': Home,
    }
    return render(request, template_name='PodCast/home.html', context=context)


def signUp(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pas']
        pas_confirm = request.POST['pas-confirm']
        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()

    # return redirect('login')
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


def episode_page(request):
    episode = Episode.objects.all()
    context = {
        'episode': episode,
    }
    return render(request, template_name='PodCast/Episode.html',context=context)


def MusicPlayer(request):
    player = MusicPlayer.objects.all()
    context = {
        'MusicPlayer': player,
    }
    return render(request, template_name='PodCast/MusicPlayer.html',context=context)


def Creator_Page(request):
    creator = Creator.objects.all()
    context = {
        'Creator': creator,
    }
    return render(request, template_name='PodCast/Creator.html',context=context)