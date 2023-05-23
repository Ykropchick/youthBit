from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.models import Hr


class IsHRUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user:
            return True
        return Hr.objects.is_user_hr(request.user)


class IsHRUser(BasePermission):
    def has_permission(self, request, view):
        return Hr.objects.is_user_hr(request.user)