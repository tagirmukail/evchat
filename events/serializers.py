from rest_framework import serializers
from .models import Event, Tag, Star


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'profile',
            'place',
            'start_date_time',
            'create_date_time',
            'update_date_time',
            'title',
            'description',
            'type',
            'delete',
        )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'text',
            'event',
            'profile'
        )


class StarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Star
        fields = (
            'count',
            'event',
            'profile'
        )
