from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .api_users import api_root, UserList, UserDetail, ProfileList, ProfileDetail, \
    PhoneList, PhoneDetail, AvatarList, AvatarDetail

urlpatterns = [
    url(r'^api/$', api_root, name='api'),

    url(r'^api/users/$', UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),

    url(r'^api/profiles/$', ProfileList.as_view(), name='profile-list'),
    url(r'^api/profiles/(?P<pk>\d+)/$', ProfileDetail.as_view(), name='profile-detail'),

    url(r'^api/phones/$', PhoneList.as_view(), name='phone-list'),
    url('^api/phones/(?P<number>\d+)/$', PhoneDetail.as_view(), name='phone-detail'),

    url('^api/avatars/$', AvatarList.as_view(), name='avatar-list'),
    url('^api/avatars/(?P<pk>\d+)/$', AvatarDetail.as_view(), name='avatar-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns += [
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
