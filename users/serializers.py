from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Phone, Avatar


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_active'
        )


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'online_status',
            'deleted'
        )


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = (
            'profile',
            'number'
        )


class AvatarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avatar
        fields = (
            'profile',
            'url',
            'title',
            'is_use',
            'delete'
        )
