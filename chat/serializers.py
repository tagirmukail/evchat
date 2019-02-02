from rest_framework import serializers
from .models import Message, Room


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id',
            'label',
            'is_online',
            'participant',
        )


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = (
            'room',
            'profile',
            'text',
            'html',
            'send_date_time',
            'delive_date_time',
        )
