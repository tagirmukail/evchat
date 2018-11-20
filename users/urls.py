from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^authentication/$', views.authentication, name='authentication'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^registration/$', views.registration, name='registration'),
]