from rest_framework import generics
from chat.models import Message, Room
from chat.serializers import MessageSerializer, RoomSerializer


class RoomList(generics.ListCreateAPIView):
    """
        Api represents a list of events.
    """
    model = Room
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateAPIView):
    model = Room
    serializer_class = RoomSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if pk:
            return Room.objects.filter(pk=pk)


class MessageList(generics.ListCreateAPIView):
    model = Message
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateAPIView):
    model = Message
    serializer_class = MessageSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if pk:
            return Message.objects.filter(pk=pk)
