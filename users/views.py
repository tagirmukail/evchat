from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, SendForm, LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "users/index.html")


def send_code(request):
    form = SendForm()

    if request.method == 'POST':
        form = SendForm(data=request.POST)
        if form.is_valid():
            form.generate_acceppted_code()

            return HttpResponseRedirect(reverse('registration'))

    context = {'form': form}
    return render(request, 'users/send_code.html', context)


def auth(request):
    login_form = LoginForm()
    if request.method == 'POST':
        try:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                login(request, login_form.profile.user)
                return HttpResponseRedirect(request.POST.get('next'))
        except ValueError as err:
            login_form.add_error("phone", err)
    context = {'form': login_form}
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
                    return HttpResponseRedirect(reverse('auth'))
        except ValueError as err:
            profile_form.add_error('accept_code', err)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)


@login_required
def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
