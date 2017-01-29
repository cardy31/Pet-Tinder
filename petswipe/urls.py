from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from petswipe import views

# app_name = 'refs'
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^member/$',
        views.MemberList.as_view(),
        name='member-list'),
    url(r'^member/(?P<pk>[0-9]+)/$',
        views.MemberDetail.as_view(),
        name='member-detail'),
    url(r'^swipedanimal/$',
        views.SwipedAnimalList.as_view(),
        name='swipedanimal-list'),
    url(r'^swipedanimal/(?P<pk>[0-9]+)/',
        views.SwipedAnimalDetail.as_view(),
        name='swipedanimal-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
