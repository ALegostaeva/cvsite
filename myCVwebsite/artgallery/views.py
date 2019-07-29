from django.shortcuts import render
import os
from django.conf import settings
from .models import Image
from .models import Project


def index(request):
    img_list = Image.objects.all()
    proj_list = Project.objects.all()
    context = {'images': img_list, 'projects': proj_list}
    return render(request, 'artgallery/artgallery.html', context)
