from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response

from .serializers import NotificationSerializer
from .models import Notification


class NotificationListView(ListModelMixin, GenericAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        notifications = Notification.objects.filter(to=user)
        return notifications

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NotificationCreateView(CreateModelMixin, GenericAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NotificationUpdateView(GenericAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        notification_id = self.kwargs['pk']
        notifications = Notification.objects.get(pk=notification_id)
        return notifications

    def patch(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, data=request.data, many=False, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
