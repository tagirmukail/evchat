from django import forms
from django.conf import settings
from .models import Event
from .exceptions import EventStartDateTimeException
import datetime


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'place',
            'description',
            'type',
        ]
        widgets = {
            'place': forms.TextInput(attrs={"type": "hidden"}),
            'type': forms.NumberInput(attrs={
                'min': settings.TYPE_CLOSE_EVENT,
                'max': settings.TYPE_OPEN_EVENT,
                'default': settings.TYPE_CLOSE_EVENT}),
            'title': forms.TextInput()
        }

        labels = {
            'place': 'Search place in map',
            'type': "Select type to event"
        }

    start_date_time = forms.DateTimeField(input_formats=[settings.DATETIME_FORMAT],
                                          label='start',
                                          widget=forms.DateTimeInput(attrs={'class': "form-control"})
                                          )

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
