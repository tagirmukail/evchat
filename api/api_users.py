from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from users.models import Profile, Phone, Avatar
from users.serializers import UserSerializer, ProfileSerializer, AvatarSerializer, PhoneSerializer


api_view(["GET"])
def api_root(request, format=None):
    """
    The entry of Api.
    :param request:
    :param format:
    :return:
    """
    return Response({
        'users': reverse('user-list', request=request)
    })


class UserList(generics.ListCreateAPIView):
    """
    Api represents a list of users
    """
    model = User
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileList(generics.ListCreateAPIView):
    """
    Api represents a list of profiles
    """
    model = Profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Api represents a single user.
    """
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return None
        return User.objects.filter(pk=pk)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Api represents a single profile.
    """
    model = Profile
    serializer_class = ProfileSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return None
        return Profile.objects.filter(pk=pk)


class PhoneList(generics.ListCreateAPIView):
    """
    Api represents a list of phones.
    """
    model = Phone
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneDetail(generics.RetrieveUpdateAPIView):
    """
    Api represents a single phone.
    """
    lookup_field = 'number'
    model = Phone
    serializer_class = PhoneSerializer

    def get_queryset(self):
        number = self.kwargs.get('number')
        if not number:
            return None
        return Phone.objects.filter(number=number)


class AvatarList(generics.ListCreateAPIView):
    """
    Api represents a list of avatars.
    """
    model = Avatar
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer


class AvatarDetail(generics.RetrieveUpdateAPIView):
    """
    Api represents a single avatar.
    """
    model = Avatar
    serializer_class = AvatarSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return None
        return Avatar.objects.filter(pk=pk)
