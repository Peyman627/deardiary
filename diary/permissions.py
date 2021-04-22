from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    custom permission to only allow owners of an object access it
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user