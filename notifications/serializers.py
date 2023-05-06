from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model

user_model = get_user_model()


class CustomUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = ('pk', 'firstname', 'lastname')


class NotificationSerializer(serializers.ModelSerializer):
    to = CustomUserInfoSerializer(many=False, read_only=True)
    to_id = serializers.IntegerField(write_only=True)
    sender = CustomUserInfoSerializer(many=False, read_only=True)
    sender_id = serializers.IntegerField(write_only=True)
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Notification
        fields = ('pk', 'title', 'description', 'to', 'to_id', 'sender', 'sender_id', 'date', 'is_read')

    def update(self, instance, validated_data):
        try:
            validated_data['to'] = user_model.objects.get(pk=validated_data.pop('to_id'))
            validated_data['sender'] = user_model.objects.get(pk=validated_data.pop('sender_id'))
        except:pass
        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data['to'] = user_model.objects.get(pk=validated_data.pop('to_id'))
        validated_data['sender'] = user_model.objects.get(pk=validated_data.pop('sender_id'))
        return super().create(validated_data)