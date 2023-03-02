from rest_framework.serializers import ModelSerializer

from .models import Module, Manual, File


class ModuleListSerializer(ModelSerializer):

    class Meta:
        model = Module
        fields = ('pk', 'name', 'description')


class ManualListSerializer(ModelSerializer):

    class Meta:
        model = Manual
        fields = ('pk', 'name', 'description')


class FileListSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ('path',)