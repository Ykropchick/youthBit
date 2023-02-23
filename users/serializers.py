from rest_framework.serializers import ModelSerializer

from .models import Contact, CustomUser


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','firstname','lastname','department',"HR_link",
'position')


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

