from django.db import models
from users.models import Profile


class Event(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    subscribe = models.ManyToManyField(Profile, related_name='subscribe')
    like = models.ManyToManyField(Profile, related_name='like')

    place = models.TextField(null=False, max_length=1000)
    title = models.TextField(null=False, max_length=250)
    description = models.TextField(max_length=3000, null=True)

    start_date_time = models.DateTimeField()
    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    type = models.IntegerField(default=0)

    delete = models.BooleanField(default=False)

    def create(self, title, description,place, type, start_date_time):
        self.title = title
        self.description = description
        self.place = place

        self.type = type

        self.start_date_time = start_date_time

    def __repr__(self):
        return """
        Id:{id},
        title:{title},
        place:{place},  
        type:{type},  
        start_date_time:{start_date_time}
        """.format(
            id=self.id,
            title=self.title,
            place=self.place,
            type=self.type,
            start_date_time=self.start_date_time
        )


class Tag(models.Model):
    text = models.CharField(null=False, max_length=400)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)


class Star(models.Model):
    count = models.IntegerField(default=0)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
