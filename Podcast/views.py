from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserManager
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


# Create your views here.


def First_page(request):
    return render(request, 'PodCast/First_page.html')


def base(request):
    return render(request, 'PodCast/base.html')


def home(request):
    epi = Episode.objects.all()
    context = {
        'epi': epi,
    }

    return render(request, template_name='PodCast/home.html', context=context)


def signup(request, user_type):
    form = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            if user_type == 'listener':
                profile.is_creator = False
                profile.save()

            # user = User.objects.create_user(username=username, email=email, password=password)
            # user.save()
            # user.profile.is_creator = True
            # user.profile.save()
            # user.save()

        return redirect('login')
    return render(request, 'PodCast/signup.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        my_user = authenticate(username=username, passward=pass1)
        if my_user != None:
            login(request, my_user)
            return redirect('home')

        else:
            return redirect('home')
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


# def upload_episode(request, user):
#     profile = user.objects.create(User=request.user)
#
#     if profile.is_creator:
#         form = EpisodeForm()
#     if request.method == 'POST':
#         form = EpisodeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = {
#         'form': form
#     }
#     return render(request, template_name='PodCast/upload_episode.html', context=context)

from django.shortcuts import render, redirect
from .forms import EpisodeForm
from .models import Profile

def upload_episode(request):
    user = request.user

    try:
        profile = user.profile  # Retrieve the profile associated with the user
    except Profile.DoesNotExist:
        profile = None

    if profile and profile.is_creator:
        if request.method == 'POST':
            form = EpisodeForm(request.POST, request.FILES)
            if form.is_valid():
                episode = form.save(commit=False)
                episode.creator = request.user
                episode.save()
                return redirect('home')
        else:
            form = EpisodeForm()
    else:
        # Handle the case where the user does not have a creator profile
        form = None  # or provide appropriate feedback to the user

    context = {'form': form}
    return render(request, 'PodCast/upload_episode.html', context)
