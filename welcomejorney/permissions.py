from rest_framework.permissions import BasePermission,SAFE_METHODS
from django.core.exceptions import ObjectDoesNotExist

from users.models import Hr
class IsHRUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user:
            return True
        hr = Hr.objects.get_hr_by_user(request.user.id)
        if not isinstance(hr,str): return True
        return False