from rest_framework.serializers import ModelSerializer
from .models import Notification
from django.contrib.auth import get_user_model

user_model = get_user_model()

class CustomUserInfoSerializer(ModelSerializer):

    class Meta:
        model = user_model
        fields = ('pk','firstname','lastname')


class NotificationListSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('pk','title','date')


class NotificationRetrieveSerializer(ModelSerializer):
    sender = CustomUserInfoSerializer(many=False,read_only=True)
    class Meta:
        model = Notification
        fields = ('title','description','sender','date')


class NotificationCreateSerializer(ModelSerializer):
    to = CustomUserInfoSerializer(many=False,read_only=True)
    sender = CustomUserInfoSerializer(many=False,read_only=True)
    class Meta:
        model = Notification
        fields = ('title','description','to','sender')