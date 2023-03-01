from rest_framework.serializers import ModelSerializer,SlugRelatedField, CharField

from .models import Contact, CustomUser, Department, Newbie,Hr

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('name','head','place')


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email','firstname','lastname','avatar')


class SubUserAbstractSerializer(ModelSerializer):
    email = CharField(write_only=True)
    password = CharField(max_length=100, write_only=True)
    firstname = CharField(max_length=30, write_only=True)
    lastname = CharField(max_length=30, write_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        abstract = True

    def create(self,validated_data):
        validated_data['user'] = CustomUser.objects.create_user(
            email=validated_data['email'], password=validated_data['password'],
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'])

        validated_data.pop('email')
        validated_data.pop('password')
        validated_data.pop('firstname')
        validated_data.pop('lastname')
        return super().create(validated_data)


class NewbieSerializer(SubUserAbstractSerializer):
    department = DepartmentSerializer(many=False,read_only=True)
    position = CharField(max_length=20)

    class Meta:
        model = Newbie
        fields = ('email','password','firstname','lastname','user','department','position')


class HrSerializer(SubUserAbstractSerializer):
    newbies = NewbieSerializer(many=True,read_only=True)

    class Meta:
        model = Hr
        fields = ('email','password','firstname','lastname','user','newbies')