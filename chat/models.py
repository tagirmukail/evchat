from django.db import models
from users.models import User

class Room(models.Model):
    name = models.TextField(null=False)
    label = models.SlugField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    online_status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __repr__(self):
        return """
        Id:{},
        Name:{},
        Label:{},
        Create Date:{},
        Online:{}""".format(
            self.id,
            self.name,
            self.label,
            self.create_date,
            self.online_status
        )

class Roster(models.Model):
    room = models.ForeignKey(Room, related_name='rooms', on_delete=False)
    user = models.ForeignKey(User, related_name='users', on_delete=False)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=False)
    user = models.ForeignKey(User, related_name='users', on_delete=False)

    message = models.TextField(null=False, max_length=3000)
    message_html = models.TextField()

    send_date = models.DateTimeField(auto_now_add=True)
    deliv_date = models.DateTimeField()

    deleted = models.BooleanField(default=False)

    def __repr__(self):
        return """
        ID:{}
        Room:{},
        User:{},
        Send Date:{},
        Deliv Date:{}""".format(
            self.id,
            self.room.id,
            self.user.id,
            self.send_date,
            self.deliv_date
        )
