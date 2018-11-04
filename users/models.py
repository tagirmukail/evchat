import bcrypt
from django.db import models

class User(models.Model):
    name = models.TextField(null=True)
    phone = models.TextField(null=False, unique=True, db_index=True)
    password = models.TextField(null=False)

    create_date_time = models.DateTimeField(auto_now_add=True)

    avatar = models.TextField(null=True)

    online_status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __init__(self, name, phone, password, avatar, online_status=False, deleted=False):
        super(User, self).__init__()
        self.name = name
        self.phone = phone
        self.password = self.gen_password(password)
        self.avatar = avatar
        self.online_status = online_status if online_status else False
        self.deleted = deleted if deleted else False

    def gen_password(self, password):
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        return hash_password

    def check_password(self, password):
        hash_password = bcrypt.hashpw(password.encode('utf-8'), self.password)

        if hash_password == self.password:
            return True

        return False

    def __repr__(self):
        user_str = """
        Id:{},
        Name:{},
        Phone:{},
        Create Date and Time:{},
        Online:{}""".format(
            self.id,
            self.name,
            self.phone,
            self.create_date_time,
            self.online_status
        )
        return user_str
