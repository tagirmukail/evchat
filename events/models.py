from django.db import models

from users.models import Profile

class Event(models.Model):

    owner = models.ForeignKey(Profile, related_name='event_owners', on_delete=models.CASCADE)

    title = models.TextField(null=False, max_length=50)
    description = models.TextField(max_length=500, null=True)

    start_date_time = models.DateTimeField()
    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    city = models.TextField(null=False)
    country = models.TextField(null=False)

    close = models.BooleanField(default=False)

    delete = models.BooleanField(default=False)

    def create(self,
                 title,
                 desctiption,
                 city,
                 country,
                 owner,
                 close,
                 create_date_time,
                 start_date_time):
        super(Event, self).create()

        self.title = title
        self.description = desctiption

        self.city = city
        self.country = country

        self.close = close

        self.owner = owner

        self.create_date_time = create_date_time
        self.start_date_time = start_date_time

    def __repr__(self):
        return """
        Id:{id},
        title:{title},  
        
        city:{city}, 
        country:{country}, 
        
        owner:{owner}, 
        
        close:{close}, 
        
        create_date_time:{create_date_time}, 
        start_date_time:{start_date_time}
        """.format(
            id=self.id,
            title=self.title,
            city=self.city,
            country=self.country,
            owner=self.owner,
            close=self.close,
            create_date_time=self.create_date_time,
            start_date_time=self.start_date_time
        )


class Subscribe(models.Model):
    subscribe_user = models.ForeignKey(Profile, related_name='subscribe_users', on_delete=models.CASCADE)

    event = models.ForeignKey(Event, related_name='subscribe_events', on_delete=models.CASCADE)

    create_date_time = models.DateTimeField(auto_now=True)

    def create(self, subscriber_user, event):
        super(Subscribe, self).create()

        self.subscribe_user = subscriber_user
        self.event = event

    def __repr__(self):
        return """
        Id:{id},
        
        Event:
        {event},
        
        Subscriber User:
        {subscriber_user},
        
        Create Date Time:{create_date_time}
        """.format(
            id=self.id,
            event=self.event,
            subscriber_user=self.subscribe_user,
            create_date_time=self.create_date_time
        )


class Like(models.Model):
    status_add = models.BooleanField(default=True)

    like_users = models.ForeignKey(Profile, related_name='like_users', on_delete=models.CASCADE)

    event = models.ForeignKey(Event, related_name='like_events', on_delete=models.CASCADE)

    create_date_time = models.DateTimeField(auto_now=True)

    def create(self, status_add, event):
        super(Like, self).create()

        self.status_add = status_add
        self.event = event

    def __repr__(self):
        return """
        Id:{id},
        Status Add:{status_add},
        
        Event:
        {event},
        
        Create Date Time:{create_date_time}
        """.format(
            id=self.id,
            status_add=self.status_add,
            event=self.event,
            create_date_time=self.create_date_time
        )

class Contact(models.Model):

    owner_profiles = models.ManyToManyField(Profile, related_name='owners')

    contact_profiles = models.ManyToManyField(Profile, related_name='contact_profiles')

    create_date_time = models.DateTimeField(auto_now_add=True)

    updated_date_time = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)

    def create(self, deleted):
        super(Contact, self).create()

        self.deleted = deleted

    def __repr__(self):
        return """
        Id:{id},
        
        Deleted:{deleted},
        
        Create Date Time:{create_date_time},
        Update Date Time:{update_date_time}
        """.format(
            id=self.id,
            deleted=self.deleted,
            create_date_time=self.create_date_time,
            update_date_time=self.updated_date_time
        )
