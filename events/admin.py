from django.contrib import admin
from .models import Event, Star, Tag

admin.site.register([Event, Star, Tag])