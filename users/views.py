from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User

def index(request):
    return HttpResponse(b'hello')

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            HttpResponseRedirect(reverse('login'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
