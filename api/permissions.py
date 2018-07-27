from rest_framework.permissions import BasePermission
from .models import Book


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
