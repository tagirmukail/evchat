from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .api_users import api_root, UserList, UserDetail, ProfileList, ProfileDetail, \
    PhoneList, PhoneDetail, AvatarList, AvatarDetail
from .api_events import EventList, EventDetail
from .api_chat import MessageList, MessageDetail, RoomList, RoomDetail

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

    # Chat api urls
    url(r'^rooms/$', RoomList.as_view(), name='room-list'),
    url(r'^rooms/(?P<pk>\d+)/$', RoomDetail.as_view(), name='room-detail'),

    url(r'^messages/$', MessageList.as_view(), name='message-list'),
    url(r'^messages/(?P<pk>\d+)/$', MessageDetail.as_view(), name='message-detail')

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += [
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
