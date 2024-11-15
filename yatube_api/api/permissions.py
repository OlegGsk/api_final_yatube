from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class OnlyGetOrPostMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method == 'GET' or request.method == 'POST')
