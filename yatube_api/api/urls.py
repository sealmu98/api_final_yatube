from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from api import views

v1_router = routers.DefaultRouter()

v1_router.register('posts', views.PostViewSet, basename='post')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   views.CommentViewSet, basename='comment')
v1_router.register('follow', views.FollowViewSet, basename='follow')
v1_router.register('groups', views.GroupViewSet, basename='groups')

v1_urls = [
    path('', include(v1_router.urls)),
    path('jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('api-token-auth/', obtain_auth_token,
         name='api_token_auth'),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
