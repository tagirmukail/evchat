from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Event, Place, Star, Tag
from users.models import Profile
from .forms import EventForm, PlaceForm

@login_required
def create_event(request):
    event_form = EventForm()
    place_form = PlaceForm()
    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        place_form = PlaceForm(data=request.POST)
        try:
            if event_form.is_valid() and place_form.is_valid():
                place = place_form.save()
                event = event_form.save(commit=False)
                event.place = place
                profile = Profile.objects.filter(user=request.user).first()
                event.profile = profile
                event.commit()
                return HttpResponseRedirect(reverse('index'))
        except Exception as exception:
            event_form.add_error('title', exception)
    context = {'event_form': event_form, 'place_form': place_form}
    return render(request, 'events/event_create.html', context)
