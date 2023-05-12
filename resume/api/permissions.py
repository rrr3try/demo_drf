from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update'] and obj.owner == request.user:
            return True
        elif view.action == 'retrieve':
            return True
        return False
