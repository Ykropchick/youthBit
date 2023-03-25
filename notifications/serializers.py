from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model

user_model = get_user_model()


class CustomUserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_model
        fields = ('pk', 'firstname', 'lastname')


class NotificationSerializer(serializers.ModelSerializer):
    to = serializers.PrimaryKeyRelatedField(queryset=user_model.objects.all())
    sender = serializers.PrimaryKeyRelatedField(queryset=user_model.objects.all())
    date = serializers.DateTimeField(read_only=True)
    is_read = serializers.BooleanField(read_only=True)

    class Meta:
        model = Notification
        fields = ('pk', 'title', 'description', 'to', 'sender', 'date', 'is_read')
