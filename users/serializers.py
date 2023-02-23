from rest_framework.serializers import ModelSerializer,SlugRelatedField

from .models import Contact, CustomUser, Department

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('name','head','place')


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class UserSerializer(ModelSerializer):
    department = DepartmentSerializer(many=False,read_only=True)

    class Meta:
        model = CustomUser
        fields = ('email','firstname','lastname','department',"HR_link",
'position')


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

