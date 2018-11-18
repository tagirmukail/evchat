from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import RegisterForm, SendForm

def index(request):
    return HttpResponse(b'hello')

def authentication(request):
    form = SendForm()
    if request.method == 'POST':

        form = SendForm(data=request.POST)
        if form.is_valid():
            form.generate_acceppted_pass()
            print(reverse('registration'))
            HttpResponseRedirect(reverse('registration'))
    context = {'form': form}
    return render(request, 'users/auth.html', context)

def registration(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            if not new_user:
                HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
