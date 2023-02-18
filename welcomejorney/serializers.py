from rest_framework.serializers import ModelSerializer
from .models import Module,Manual


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = ('pk','name','description','department')

class ManualSerializer(ModuleSerializer):
    class Meta:
        model = Manual
        fields = ('name','link','module')