"""
URL configuration for BC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Podcast import views as p_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', p_views.home, name='home'),
    # path('', p_views.base, name='base'),
    path('', p_views.First_page, name='First_page'),
    path('upload_episode/', p_views.upload_episode, name='upload_episode'),
    path('player/<str:id>', p_views.player, name='player'),
    path('delete_epi/<str:id>', p_views.delete_epi, name='delete_epi'),
    path('signUpCreator', p_views.signUpCreator, name='signUpCreator'),
    path('signUpListener', p_views.signUpListener, name='signUpListener'),
    path('login', p_views.loginUser, name='login'),
    path('logOut', p_views.logOut, name='logOut'),
    path('userPage', p_views.userPage, name='userPage'),
    path('ArtistPage/', p_views.ArtistPage, name='ArtistPage'),
    path('Episode/', p_views.episode_page, name='Episode'),
    # path('MusicPlayer/', p_views.MusicPlayer, name='MusicPlayer'),
    path('Creator/', p_views.Creator_Page, name='Creator'),
    path("mock-payment/", p_views.mock_payment, name="mock_payment"),
    path("premium/", p_views.premium, name="premium"),
    path('more/', p_views.more_option, name='more_option'),
    path('make-payment/', p_views.make_payment, name='make_payment'),
    path('process-payment/', p_views.process_payment, name='process_payment'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
