from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from events.models import Event, Tag, Star
from events.serializers import EventSerializer, TagSerializer, StarSerializer


class EventList(generics.ListCreateAPIView):
    """
    Api represents a list of events.
    """
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateAPIView):
    """
    Api represents a single Event.
    """
    model = Event
    serializer_class = EventSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return None
        return Event.objects.filter(pk=pk)
