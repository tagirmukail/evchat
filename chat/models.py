from django.db import models
from users.models import Profile

class Room(models.Model):
    name = models.TextField(null=False)
    label = models.SlugField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    online_status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def create(self, name, label, deleted=False, online_status=False):
        self.name = name
        self.label = label
        self.deleted = deleted if deleted else False
        self.online_status = online_status if online_status else False

    @property
    def group_name(self):
        return "room-{}".format(self.id)

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
    room = models.ManyToManyField(Room, related_name='rooms')
    user = models.ManyToManyField(Profile, related_name='users')

    def __repr__(self):
        return """
        Id:{id},
        
        Room:{room},
        
        User:{user}
        """.format(
            id=self.id,
            room=self.room,
            user=self.user
        )

    def __str__(self):
        return """
                Id:{id},

                Room:{room},

                User:{user}
                """.format(
            id=self.id,
            room=self.room,
            user=self.user
        )

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='message_rooms', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='message_users', on_delete=models.CASCADE)

    message = models.TextField(null=False, max_length=3000)
    message_html = models.TextField()

    send_date = models.DateTimeField(auto_now_add=True)
    delive_date = models.DateTimeField()

    deleted = models.BooleanField(default=False)

    def create(self, room, user, message, message_html, delive_date, deleted):
        self.room = room
        self.user = user

        self.message = message
        self.message_html = message_html

        self.delive_date = delive_date

        self.deleted = deleted

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
            self.delive_date
        )
