from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, SendForm

def index(request):
    return HttpResponse(b'hello')

def authentication(request):
    form = SendForm()

    if request.method == 'POST':
        form = SendForm(data=request.POST)
        if form.is_valid():
            form.generate_acceppted_code()

            return HttpResponseRedirect(reverse('registration'))

    context = {'form': form}
    return render(request, 'users/auth.html', context)

def registration(request):
    user_form = UserCreationForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        try:
            if user_form.is_valid() and profile_form.is_valid():
                new_user = user_form.save()
                new_profile = profile_form.save(commit=False)
                new_profile.user = new_user
                new_profile.save()
                if new_user and new_profile:
                    return HttpResponseRedirect(reverse('index'))
        except ValueError as err:
            profile_form.add_error('accept_code', err)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
