from django.core.paginator import Paginator
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


def base(request):
    return render(request, 'PodCast/base.html')


def home(request):
    epi = Episode.objects.all()
    context = {
        'epi': epi,
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
    return render(request, template_name='PodCast/userPage.html')


def ArtistPage(request):
    return render(request, template_name='PodCast/ArtistPage.html')


def episode_page(request):
    episode = Episode.objects.all()
    context = {
        'episode': episode,
    }
    return render(request, template_name='PodCast/Episode.html', context=context)


def player(request, id):
    player = Episode.objects.get(pk=id)
    context = {
        'player': player,
    }
    return render(request, template_name='PodCast/audio.html', context=context)


def Creator_Page(request):
    creator = Creator.objects.all()
    context = {
        'Creator': creator,
    }
    return render(request, template_name='PodCast/Creator.html', context=context)


def index(request):
    queryset = Audio.objects.all().order_by('title')
    paginator = Paginator(queryset, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, 'PodCast/index.html', context)
