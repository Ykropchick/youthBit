from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsHRUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user:
            return True
        return bool(request.user and request.user.is_HR)