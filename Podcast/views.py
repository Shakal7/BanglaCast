import random
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from .forms import *


# Create your views here.


def First_page(request):
    # Fetch recent episodes excluding premium ones
    recent = list(Episode.objects.filter(is_premium=False).order_by('-date_added')[:7])

    # Fetch popular episodes excluding premium ones
    popular = list(Episode.objects.filter(is_premium=False).order_by('-plays')[:3])

    # Combine recent and popular episodes while avoiding duplicates
    combined = recent.copy()
    for ep in popular:
        if ep not in combined:
            combined.append(ep)

    # Limit the episodes to show to 10
    episodes_to_show = combined[:10]

    # Pass the episodes to the template
    context = {
        'episodes': episodes_to_show
    }

    return render(request, 'PodCast/First_page.html', context)


# def Explore(request):
#     episodes = Episode.objects.filter(is_premium=False)
#     return render(request, 'PodCast/Explore.html', {
#         'episodes': episodes
#     })


def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            playlist = form.save()

            return redirect('home')
    else:
        form = PlaylistForm()
    return render(request, 'PodCast/create_playlist.html', {'form': form})


# def update_episode_premium_status(playlist):
#     episodes = playlist.episodes.order_by('id')
#     for index, ep in enumerate(episodes):
#         if index < 2:
#             ep.is_premium = False
#         else:
#             ep.is_premium = True
#         ep.save()


def Playlist_view(request):
    category = request.GET.get('category')

    if category:
        playlists = Playlist.objects.filter(category__iexact=category)  # Case-insensitive match
    else:
        playlists = Playlist.objects.all()

    return render(request, 'PodCast/playlist_view.html', {'playlists': playlists})


def home(request):
    if not request.user.is_authenticated:
        return redirect('msg')

    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    playlists = Playlist.objects.all()
    view_all = request.GET.get('view') == 'all'
    category = request.GET.get('category')  # For filtering

    # Filter episodes
    episodes = Episode.objects.filter(is_premium=False)

    if category:
        episodes = episodes.filter(category__iexact=category)

    if view_all and (request.user.profile.is_premium or request.user.profile.is_creator):
        episodes = Episode.objects.all()
        if category:
            episodes = episodes.filter(category__iexact=category)

    # Limit for free user
    # if not (request.user.profile.is_premium or request.user.profile.is_creator):
    #     episodes = episodes[:2]

    context = {
        'playlists': playlists,
        'episodes': episodes,
        'view_all': view_all,
        'category': category,
        'is_more_page': False,
    }

    return render(request, 'PodCast/home.html', context)


def playlist_details(request, id):
    playlist = get_object_or_404(Playlist, id=id)
    episodes = playlist.episodes.all()
    return render(request, 'PodCast/playlist_details.html', {
        'playlist': playlist,
        'episodes': episodes
    })


def episode_detail(request, id):
    episode = Episode.objects.get(id=id)
    return render(request, 'PodCast/episode_detail.html', {'episode': episode})


def upload_episode(request):
    user = request.user

    # Assuming Profile model has a OneToOneField with User model
    try:
        profile = user.profile  # Retrieve the profile associated with the user
    except Profile.DoesNotExist:
        # Handle the case where the profile doesn't exist (optional)
        profile = None

    if profile and profile.is_creator:
        form = EpisodeForm()

        if request.method == 'POST':
            form = EpisodeForm(request.POST, request.FILES)
            if form.is_valid():
                # Assuming the episode model is being created and associated with the user
                episode = form.save(commit=False)
                episode.creator = request.user  # Assign the current user as the creator
                episode.save()
                return redirect('home')  # Redirect to home page after successful form submission

    else:
        # Handle the case where the user does not have a creator profile
        form = None  # or provide appropriate feedback to the user

    context = {
        'form': form
    }
    return render(request, 'PodCast/upload_episode.html', context)


def base(request):
    return render(request, 'PodCast/base.html')


def episode_page(request):
    episode = Episode.objects.all()
    context = {
        'episode': episode,
    }
    return render(request, template_name='PodCast/Episode.html', context=context)


def userPage(request):
    return render(request, template_name='PodCast/userPage.html')


def ArtistPage(request):
    return render(request, template_name='PodCast/ArtistPage.html')


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


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile


def signUpListener(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword and len(password) >= 3:
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()
            profile = Profile.objects.create(user=user, is_creator=False)
            profile.save()
            return redirect('/')
    return render(request, 'PodCast/signup.html', {'is_creator': False})


def signUpCreator(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword and len(password) >= 3:
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()

            # Subscription plan only for Creator
            subscription_plan = request.POST.get('subscription_plan', '')

            profile = Profile.objects.create(user=user, is_creator=True, subscription_plan=subscription_plan)
            profile.save()
            return redirect('/')

    return render(request, 'PodCast/signup.html', {'is_creator': True})


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

                try:
                    profile = Profile.objects.get(user=user)
                    if profile.is_creator:
                        return redirect('home')  # creator.html er URL name
                    else:
                        return redirect('home')
                except Profile.DoesNotExist:
                    print("Profile does not exist!")

            else:
                print("Invalid credentials!")

        return render(request, 'PodCast/login.html')


def profileView(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'PodCast/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def logOut(request):
    auth.logout(request)
    return redirect('/')


@login_required
def mock_payment(request):
    profile = Profile.objects.filter(user=request.user).first()

    if not profile:
        messages.error(request, "")
        return redirect("home")

    if profile.is_creator:
        messages.error(request, "")
        return redirect("PodCast/premium")

    return render(request, "PodCast/mock_payment.html")


@login_required
def premium(request):
    profile = Profile.objects.filter(user=request.user).first()

    if profile.is_creator:
        return render(request, "premium_creator.html")  # Different page for creators

    if not profile or not profile.is_premium_active():
        messages.error(request, "⚠️ Your premium subscription has expired! Please renew.")
        return redirect("PodCast/mock_payment")

    return render(request, "PodCast/premium.html", {"profile": profile})


def more_option(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')

    # Ensure the user has a profile
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    # Fetch episodes based on user type
    if request.user.profile.is_premium or request.user.profile.is_creator:
        # Fetch all episodes for premium users or creators
        episodes = Episode.objects.all()
    else:
        # Restrict to free episodes for regular users
        episodes = Episode.objects.filter(is_premium=False)

    context = {
        'episodes': episodes,
        'is_more_page': True,  # Add this to indicate the request is for the more page
    }
    return render(request, 'PodCast/home.html', context)


@login_required
def process_payment(request):
    if request.method == "POST":
        subscription = request.POST.get("subscription")
        status = "success"  # mock payment, so it's always success

        profile = request.user.profile

        if status == "success":
            if subscription == "weekly":
                profile.is_premium = True
                profile.expiry_date = datetime.now() + timedelta(weeks=1)
            elif subscription == "monthly":
                profile.is_premium = True
                profile.expiry_date = datetime.now() + timedelta(days=30)
            elif subscription == "yearly":
                profile.is_premium = True
                profile.expiry_date = datetime.now() + timedelta(days=365)

            profile.save()

            # ✅ Correct way to pass parameters via query string
            return redirect(
                f'/make-payment/?payment_status=success&expiry_date={profile.expiry_date.strftime("%Y-%m-%d")}')
        else:
            return redirect('/make-payment/?payment_status=failed')


def make_payment(request):
    payment_status = request.GET.get('payment_status', 'failed')
    expiry_date = request.GET.get('expiry_date', None)

    return render(request, "PodCast/make_confirmation.html", {
        'payment_status': payment_status,
        'expiry_date': expiry_date
    })


def search_episodes(request):
    query = request.GET.get('s', '')  # Get the query from the search form
    # Use Title instead of title
    episodes = Episode.objects.filter(Title__icontains=query) if query else Episode.objects.all()
    return render(request, 'PodCast/home.html', {'episodes': episodes, 'query': query})


def player(request, id):
    player = get_object_or_404(Episode, id=id)

    if player.playlist:
        all_episodes = Episode.objects.filter(playlist=player.playlist).order_by('id')
        episode_list = list(all_episodes)
        player_index = episode_list.index(player) + 1  # 1-based index
    else:
        player_index = 1

        # Premium check
    is_premium_user = False
    if request.user.is_authenticated:
        profile = getattr(request.user, 'profile', None)
        if profile:
            is_premium_user = profile.is_premium

    # Can play logic
    # can_play = (player_index <= 2) or is_premium_user

    context = {
        'player': player,
        # 'can_play': can_play,
        'is_premium_user': is_premium_user,
        'player_index': player_index,
    }
    return render(request, 'PodCast/audio.html', context=context)
