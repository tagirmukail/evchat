from django import forms
from django.conf import settings
from .models import Event
from .exceptions import EventPlaceException, EventStartDateTimeException
import datetime


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'place',
            'description',
            'start_date_time',
            'type',
        ]
        widgets = {
            'place': forms.TextInput(attrs={"type": "hidden"}),
            'start_date_time': forms.DateTimeInput(format=settings.DATETIME_FORMAT, attrs={'class': "form-control"}),
            'type': forms.NumberInput(attrs={'min': 0, 'max': 1, 'default': 0}),
            'title': forms.TextInput()
        }

        labels = {
            'start_date_time': 'Start',
            'place': 'Search place in map',
            'type': "Select type to event"
        }

    def is_valid(self):
        super(EventForm, self).is_valid()
        return self.is_valid_start_dtime()

    def is_valid_start_dtime(self):
        dt_event = self.cleaned_data.get('start_date_time')
        event_info = dt_event.astimezone().tzinfo
        now = datetime.datetime.now(tz=event_info)
        if now > dt_event:
            raise EventStartDateTimeException("Event cannot be earlier than current date.")
        return True
