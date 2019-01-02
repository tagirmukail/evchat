import bcrypt
from django.contrib.auth.models import User
from django.db import models
from .helpers import Helper


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    create_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    online_status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def create(self, online_status=False, deleted=False):
        super(Profile, self).create()
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
        Create Date and Time:{},
        Online:{},
        Delete:{}""".format(
            self.id,
            self.user,
            self.create_date_time,
            self.online_status,
            self.deleted
        )
        return profile_str


class Phone(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    number = models.TextField(null=False, unique=True)
    contact = models.ManyToManyField(Profile, related_name="contact")

    @staticmethod
    def get_phones(profile):
        return Phone.objects.filter(profile=profile).all()

    @staticmethod
    def add_phone(profile, number):
        phone = Phone()
        phone.profile = profile
        phone.number = number
        return phone

    def __str__(self):
        return """
        ID:{},
        Number:{}
        """.format(
            self.id,
            self.number
        )


class Avatar(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    url = models.URLField(null=False, unique=True)
    title = models.TextField(max_length=255)
    is_use = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return """
        ID:{},
        URL:{},
        Title:{},
        IS USE:{},
        Delete:{}
        """.format(
            self.id,
            self.url,
            self.title,
            self.is_use,
            self.delete
        )
