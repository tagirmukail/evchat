from django.db import models

class User(models.Model):
    name = models.TextField(null=True)
    phone = models.TextField(null=False, unique=True, db_index=True)
    password = models.TextField(null=False)

    create_date = models.DateTimeField(auto_created=True,
                                       auto_now=True)
    online_status = models.BooleanField(default=False)

    avatar = models.TextField(null=True)

    def __str__(self):
        user_str = """
        Id:{},
        Name:{},
        Phone:{},
        Create Date:{},
        Online:{}""".format(
            self.id,
            self.name,
            self.phone,
            self.create_date,
            self.online_status
        )
        return user_str
