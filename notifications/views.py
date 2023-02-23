from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from .serializers import NotificationListSerializer, NotificationRetrieveSerializer
from .models import Notification

class NotificationListView(ListModelMixin,GenericAPIView):
    serializer_class = NotificationListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        notifications = Notification.objects.filter(to=user)
        return notifications

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class NotificationDetailView(RetrieveModelMixin,GenericAPIView):
    serializer_class = NotificationRetrieveSerializer

    def get_queryset(self):
        user = self.request.user
        notifications = Notification.objects.filter(to=user)
        return notifications

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)



