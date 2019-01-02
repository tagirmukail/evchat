from django import forms
from .models import Event, Place, Tag, Star
import datetime


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'start_date_time',
        ]

    title = forms.CharField(max_length=250, label='Title')
    start = forms.DateTimeField(label='Start', widget=forms.DateTimeInput())

    def is_valid(self):
        super(EventForm, self).is_valid()


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = [
            'city',
            'country',
            # 'description'
        ]

    city = forms.CharField(max_length=250, label='City')
    country = forms.CharField(max_length=250, label='Country')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'text'
        ]


class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = [
            'count'
        ]
