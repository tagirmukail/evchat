from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from users.serializers import UserSerializer, ProfileSerializer, AvatarSerializer, PhoneSerializer

