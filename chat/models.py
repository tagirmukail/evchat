from django.db import models
from users.models import Profile


class Room(models.Model):
    label = models.TextField(unique=True, null=False)
    create_date_time = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=False, null=False)
    is_delete = models.BooleanField(default=False, null=False)
    participant = models.ManyToManyField(Profile, related_name='participant')

    def create(self, label):
        self.label = label

    @property
    def group_name(self):
        return "room-{}".format(self.id)

    def __repr__(self):
        return """
        Id:{},
        Label:{},
        Create Date:{},
        Online:{}
        Delete:{}""".format(
            self.id,
            self.label,
            self.create_date,
            self.is_online,
            self.is_delete
        )


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='rooms', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='profiles', on_delete=models.CASCADE)

    text = models.TextField(null=False, max_length=3000)
    html = models.TextField(null=False, max_length=6000)

    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    send_date_time = models.DateTimeField()
    delive_date_time = models.DateTimeField()

    delete = models.BooleanField(default=False)

    def create(self, text, html, delive_date_time, send_date_time, delete):
        self.text = text
        self.html = html

        self.send_date_time = send_date_time
        self.delive_date_time = delive_date_time

        self.delete = delete

    def __repr__(self):
        return """
        ID:{}
        Text:{},
        HTML:{},
        Send Date Time:{},
        Deliv Date Time:{}""".format(
            self.id,
            self.text[:50] if len(self.text) > 50 else self.text,
            self.html[:60] if len(self.html) > 60 else self.html,
            self.send_date_time,
            self.delive_date_time
        )
