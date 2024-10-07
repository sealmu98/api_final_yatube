from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from api.permissions import IsOwnerOrReadOnly, CustomCommentPermission, CustomPostPermission, CustomFollowPermission
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer
from posts.models import Group, Post, Follow


class AuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'error': 'No data provided'}, status=400)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if not serializer.is_valid():
            if 'username' in serializer.errors or 'password' in serializer.errors:
                return Response(serializer.errors, status=401)
            else:
                return Response(serializer.errors, status=400)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })


class RefreshTokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    permission_classes = []

    def create(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token is None:
            return Response({'error': 'Refresh token is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            token = Token.objects.get(key=refresh_token)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid refresh token'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = token.user
        new_token = Token.objects.create(user=user)
        return Response({'token': new_token.key})


class VerifyTokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    permission_classes = []

    def create(self, request):
        token = request.data.get('token')
        if token is None:
            return Response({'error': 'Token cannot be None'}, status=400)
        try:
            Token.objects.get(key=token)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=400)
        return Response({'message': 'Token is valid'})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [CustomPostPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [CustomCommentPermission]

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [CustomFollowPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class JWTViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    def verify(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']
        # Проверить токен
        return Response({'token': token})
