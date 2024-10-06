from django.urls import include, path
from rest_framework import routers

from api import views

v1_router = routers.DefaultRouter()

v1_router.register('posts', views.PostViewSet, basename='post')
v1_router.register('groups', views.GroupViewSet, basename='groups')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   views.CommentViewSet, basename='comment')

v1_urls = [
    path('', include(v1_router.urls)),
    path('api-token-auth/', views.AuthToken.as_view(),
         name='api-token-auth'),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
