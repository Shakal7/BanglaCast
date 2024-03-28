from django.shortcuts import render
from .models import *


# Create your views here.

def episode(request):

     podcast = Episode.objects.all()
     context= {
        'podcast': podcast,
    }
    return render(request, template_name='PodCast/Episode.html', context=context)

