from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from users.models import Profile

@login_required
def index(request):
    user = request.user.id
    profile = Profile.objects.filter(user=user).first()
    rooms = []
    if profile:
        rooms = Room.objects.filter(profiles=profile)

    context = {"rooms": rooms}
    return render(request, "chat/index.html", context)
