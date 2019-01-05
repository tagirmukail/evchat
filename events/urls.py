from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^event/(?P<event_id>[0-9]+)/$', views.event, name='event')
]