from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import (NotificationListSerializer,
NotificationRetrieveSerializer, NotificationCreateSerializer)
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

class NotificationCreateView(CreateModelMixin,GenericAPIView):
    serializer_class = NotificationCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        to_pk = self.request.POST['to']
        to_obj = get_user_model().objects.get(pk=to_pk)
        serializer.save(sender=self.request.user, to=to_obj)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


