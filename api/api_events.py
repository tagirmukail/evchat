from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from events.models import Event, Tag, Star
from events.serializers import EventSerializer, TagSerializer, StarSerializer