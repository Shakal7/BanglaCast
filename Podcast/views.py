from django.shortcuts import render
from .models import *


# Create your views here.

def Podcast(request):
    # podcast = Podcast.objects.all()
    # context = {
    #     'podcast': podcast,
    # }
    return render(request, template_name='PodCast/Episode.html')