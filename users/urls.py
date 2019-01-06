from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^send_code/$', views.send_code, name='send_code'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^auth/$', views.auth, name='auth'),
]