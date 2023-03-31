from rest_framework import serializers

from .models import Module, Manual


class ModuleSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = Module
        fields = ('pk', 'department', 'name', 'description')


class ManualSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = Manual
        fields = ('pk', 'module', 'name', 'description', 'file')
