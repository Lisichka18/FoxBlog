from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Articles


def create_articles(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.creator = request.user
            temp.save()
            return redirect('account')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()
    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'blog/create_articles.html', context)


# def update_articles(request):
#     error = ''
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST)
#         if form.is_valid():
#             # temp = form.save(commit=False)
#             # temp.creator = request.user
#             # temp.save()
#             name = form.cleaned_data.get("name")
#             content = form.cleaned_data.get("content")
#             Articles.objects.filter(id=request.id).update(name=name, content=content)
#             return redirect('account')
#         else:
#             error = 'Форма была неверной'
#
#     form = ArticlesForm()
#     context = {
#         'form': form,
#         'error': error,
#     }
#
#     return render(request, 'blog/update_articles.html', context)
