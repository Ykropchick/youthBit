from rest_framework import serializers
from .models import Notification

class NotificationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('pk','title','date')

class NotificationRetrieveSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField
    class Meta:
        model = Notification
        fields = ('title','description','sender','date')