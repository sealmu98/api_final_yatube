# yatube_api/api/permissions.py

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        return obj.author == request.user


class CustomCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        if request.method in ['PUT', 'PATCH']:
            return obj.author == request.user
        if request.method == 'DELETE':
            return obj.author == request.user


class CustomPostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST':
            if request.user.is_authenticated:
                if 'text' in request.data:
                    return True
                else:
                    return False
            else:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.author == request.user
        return True


class CustomFollowPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if not request.user.is_authenticated:
                raise PermissionDenied
            return True
        if request.method == 'POST':
            if not request.user.is_authenticated:
                raise PermissionDenied
            if 'following' not in request.data:
                return False
            return True
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
