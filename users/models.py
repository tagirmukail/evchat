import bcrypt
from django.contrib.auth.models import User
from django.db import models
from .helpers import Helper

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.TextField(null=False, unique=True, db_index=True)
    avatar = models.TextField(null=True, blank=True)

    create_date_time = models.DateTimeField(auto_now_add=True)

    online_status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __init__(self, phone, avatar=None, online_status=False, deleted=False):
        super(Profile, self).__init__()
        self.phone = phone
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

    def set_token(self):
        helper = Helper()
        return helper.generate_sha256_hash(self.phone)

    def __repr__(self):
        profile_str = """
        Id:{},
        User:{},
        Phone:{},
        Create Date and Time:{},
        Online:{},
        Deleted:{}""".format(
            self.id,
            self.user,
            self.phone,
            self.create_date_time,
            self.online_status,
            self.deleted
        )
        return profile_str
