from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .api_users import api_root, UserList, UserDetail, ProfileList, ProfileDetail, \
    PhoneList, PhoneDetail, AvatarList, AvatarDetail
from .api_events import EventList, EventDetail


urlpatterns = [
    url(r'^api/$', api_root, name='api'),

    # Users api urls
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),

    url(r'^profiles/$', ProfileList.as_view(), name='profile-list'),
    url(r'^profiles/(?P<pk>\d+)/$', ProfileDetail.as_view(), name='profile-detail'),

    url(r'^phones/$', PhoneList.as_view(), name='phone-list'),
    url('^phones/(?P<number>\d+)/$', PhoneDetail.as_view(), name='phone-detail'),

    url(r'^avatars/$', AvatarList.as_view(), name='avatar-list'),
    url(r'^avatars/(?P<pk>\d+)/$', AvatarDetail.as_view(), name='avatar-detail'),

    # Events api urls
    url(r'^events/$', EventList.as_view(), name='event-list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += [
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
