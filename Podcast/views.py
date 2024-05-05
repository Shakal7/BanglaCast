from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserManager
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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


def upload_episode(request):
    form = EpisodeForm()
    if request.method == 'POST':
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, template_name='PodCast/upload_episode.html', context=context)


def signUpListener(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword and len(password) >= 3:
            user = User.objects.create_user(email=email, username=username, password=password)
            user.save()
            return redirect('/')

    # return redirect('login')
    return render(request, 'PodCast/signup.html')


def signUpCreator(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword and len(password) >= 3:
            user = User.objects.create_user(email=email, username=username, password=password)
            user.save()
            profile = Profile.objects.create(user=user, is_creator=True)
            profile.save()
            return redirect('/')

    # return redirect('login')
    return render(request, 'PodCast/signup.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print("Not valid !")


        return render(request,'podcast/login.html')

def logOut(request):
    auth.logout(request)
    return redirect('/')

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


def delete_epi(request, id):
    epi = Episode.objects.get(pk=id)
    if request.method == 'POST':
        epi.delete()
        return redirect('home')
    context = {'epi': epi}

    return render(request, template_name='PodCast/delete_epi.html', context=context)



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
