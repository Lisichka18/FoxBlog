from django.shortcuts import render

from blog.models import Articles


def index(request):
    posts = Articles.objects.all()
    return render(request, 'main/index.html', {'posts': posts})


def about(request):
    return render(request, 'main/about.html')
