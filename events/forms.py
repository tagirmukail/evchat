from django import forms
from django.conf import settings
from .models import Event
from django.conf.global_settings import DATETIME_INPUT_FORMATS
from .exceptions import EventPlaceException, EventStartDateTimeException
import datetime


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'place',
            'description',
            # 'start_date_time',
            'type',
        ]
        widgets = {
            'place': forms.TextInput(attrs={"type": "hidden"}),
            # 'start_date_time': forms.DateTimeInput(format=settings.DATETIME_FORMAT, attrs={'class': "form-control"}),
            'type': forms.NumberInput(attrs={'min': 0, 'max': 1, 'default': 0}),
            'title': forms.TextInput()
        }

        labels = {
            # 'start_date_time': 'Start',
            'place': 'Search place in map',
            'type': "Select type to event"
        }

        input_formats = {
            # 'start_date_time': DATETIME_INPUT_FORMATS
        }

    start_date_time = forms.DateTimeField(input_formats=[settings.DATETIME_FORMAT], label='start', widget=forms.DateTimeInput(attrs={'class': "form-control"}))

    def is_valid(self):
        super(EventForm, self).is_valid()
        return self.is_valid_start_dtime()

    def is_valid_start_dtime(self):

        dt_event = self.cleaned_data.get('start_date_time')
        print(self.cleaned_data)
        if not dt_event:
            return False
        event_info = dt_event.astimezone().tzinfo
        now = datetime.datetime.now(tz=event_info)
        if now > dt_event:
            raise EventStartDateTimeException("Event cannot be earlier than current date.")
        return True

    def save(self, commit=True):
        event = Event()
        event.create(
            self.cleaned_data.get('title', ''),
            self.cleaned_data.get('description', ''),
            self.cleaned_data.get('place', ''),
            self.cleaned_data.get('type', 0),
            self.cleaned_data.get('start_date_time')
        )
        if commit:
            event.save()
        return event
