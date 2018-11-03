from channels.db import database_sync_to_async

from .models import Room

@database_sync_to_async
def get_room_or_error(room_id, user):
    if not user.is_authenticated:
        raise Exception("USER has to login")

    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist():
        raise Exception("Room invalid")

    if room.staff_only and not user.is_staff:
        raise Exception("Room access denied")

    return room