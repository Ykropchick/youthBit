from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet

from .serializers import NotificationSerializer
from welcomejorney.permissions import IsHRUserOrReadOnly
from .models import Notification

class NotificationViewSet(ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (IsHRUserOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        notifications = Notification.objects.filter(to=user)
        return notifications

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user.pk)



