from django.db import models

from users.models import User

class Event(models.Model):

    owner = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)

    title = models.TextField(null=False, max_length=50)
    description = models.TextField(max_length=500, null=True)

    start_date_time = models.DateTimeField()
    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    city = models.TextField(null=False)
    country = models.TextField(null=False)

    close = models.BooleanField(default=False)

    delete = models.BooleanField(default=False)

    def __init__(self,
                 title,
                 desctiption,
                 city,
                 country,
                 owner,
                 close,
                 create_date_time,
                 start_date_time):
        super(Event, self).__init__()

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
    subscribe_user = models.ForeignKey(User, related_name='users', on_delete=False)

    event = models.ForeignKey(Event, related_name='events', on_delete=False)

    create_date_time = models.DateTimeField(auto_now=True)

    def __init__(self, subscriber_user, event):
        super(Subscribe, self).__init__()

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

    event = models.ForeignKey(Event, related_name='events', on_delete=False)

    create_date_time = models.DateTimeField(auto_now=True)

    def __init__(self, status_add, event):
        super(Like, self).__init__()

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

    owner_user = models.ForeignKey(User, related_name='users', on_delete=False)

    contact_user = models.ForeignKey(User, related_name='users', on_delete=False)

    create_date_time = models.DateTimeField(auto_now_add=True)

    updated_date_time = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)

    def __init__(self, owner_user, contact_user, deleted):
        super(Contact, self).__init__()

        self.owner_user = owner_user
        self.contact_user = contact_user
        self.deleted = deleted

    def __repr__(self):
        return """
        Id:{id},
        
        Owner User:
        {owner_user},
        
        Contact User:
        {contact_user},
        
        Deleted:{deleted},
        
        Create Date Time:{create_date_time},
        Update Date Time:{update_date_time}
        """.format(
            id=self.id,
            owner_user=self.owner_user,
            contact_user=self.contact_user,
            deleted=self.deleted,
            create_date_time=self.create_date_time,
            update_date_time=self.updated_date_time
        )
