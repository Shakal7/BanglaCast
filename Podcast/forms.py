from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        fields = ('Title', 'Artist', 'Type', 'image', 'audio_files')


#for creator
class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


#for listener
# class signupForm2(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')