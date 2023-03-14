from django.shortcuts import render, redirect
from .forms import ArticlesForm
from django.contrib.auth import authenticate
from .models import Articles


def create_articles(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            # Articles.objects.create(request.form.name, request.form.content, request.user.id)
            form.save()
            return redirect('account')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'blog/create_articles.html', context)

