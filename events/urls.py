from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_event/$', views.create_event, name='create_event'),
]