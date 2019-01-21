from django.contrib import admin
from .models import Profile, Avatar, Phone

admin.site.register([Phone, Profile, Avatar])