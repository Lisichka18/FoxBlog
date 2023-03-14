from django.contrib.auth import authenticate, login
from users.forms import UserCreationForm
from django.shortcuts import render, redirect
from blog.models import Articles
from django.views import View


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password1=password1)
            user = form.save()
            login(request, user)
            return redirect('account')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class Account(View):
    template_name = 'users/account.html'

    def get(self, request):
        posts = Articles.objects.all()
        return render(request, self.template_name, {'posts': posts})
