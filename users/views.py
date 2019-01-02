from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login
from .forms import ProfileForm, SendForm
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

            return HttpResponseRedirect(reverse('auth'))

    context = {'form': form}
    return render(request, 'users/send_code.html', context)


def auth(request):
    profile_form = ProfileForm()

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        try:
            if profile_form.is_valid():
                profile = profile_form.get_profile_by_phone()
                if profile:
                    login(request, profile.user)
                    return HttpResponseRedirect(reverse('index'))
                new_profile = profile_form.save()
                if new_profile:
                    login(request, new_profile.user)
                    return HttpResponseRedirect(reverse('index'))
        except ValueError as err:
            profile_form.add_error('accept_code', err)

    context = {'form': profile_form}
    return render(request, 'users/auth.html', context)


@login_required
def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
