from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .models import Event, Star, Tag
from users.models import Profile
from .forms import EventForm
from .exceptions import EventStartDateTimeException

@login_required
def create_event(request):
    event_form = EventForm()
    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        try:
            if event_form.is_valid():
                event = event_form.save(commit=False)
                profile = Profile.objects.filter(user=request.user).first()
                event.profile = profile
                event.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                print(event_form.errors)
        except EventStartDateTimeException as exception:
            event_form.add_error('start_date_time', exception)
    context = {'event_form': event_form}
    return render(request, 'events/event_create.html', context)

@login_required
def event(request, event_id):
    event = Event.objects.filter(id=event_id).first()
    if not event:
        return Http404("This event not found")
    return render(request, 'events/event.html', context={'event': event})
