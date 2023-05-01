from rest_framework.serializers import ModelSerializer, CharField, IntegerField

from .models import CustomUser, Department, Newbie, Hr


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'head', 'place')


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'firstname', 'lastname', 'avatar')


class SubUserAbstractSerializer(ModelSerializer):
    email = CharField(write_only=True)
    password = CharField(max_length=100, write_only=True)
    firstname = CharField(max_length=30, write_only=True)
    lastname = CharField(max_length=30, write_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        abstract = True

    def create(self, validated_data):
        validated_data['user'] = CustomUser.objects.create_user(
            email=validated_data.pop('email'), password=validated_data.pop('password'),
            firstname=validated_data.pop('firstname'),
            lastname=validated_data.pop('lastname'))
        return super().create(validated_data)


class NewbieRelatedSerializer(SubUserAbstractSerializer):
    department = DepartmentSerializer(many=False)
    position = CharField(max_length=20)

    class Meta:
        model = Newbie
        fields = ('user', 'department', 'position')


class HrSerializer(SubUserAbstractSerializer):
    newbies = NewbieRelatedSerializer(many=True, read_only=True)

    class Meta:
        model = Hr
        fields = ('email', 'password', 'firstname', 'lastname', 'user', 'newbies')


class HrRelatedSerializer(SubUserAbstractSerializer):
    class Meta:
        model = Hr
        fields = ('user',)


class NewbieSerializer(SubUserAbstractSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    department_id = IntegerField(write_only=True)
    position = CharField(max_length=20)
    hr = HrRelatedSerializer(many=False, read_only=True)
    hr_id = IntegerField(write_only=True)

    class Meta:
        model = Newbie
        fields = ('email', 'password', 'firstname', 'lastname', 'user',
                  'department', 'position', 'hr', 'department_id', 'hr_id')

    def create(self, validated_data):
        validated_data['department'] = Department.objects.get(pk=
                                                              validated_data.pop('department_id'))
        validated_data['hr'] = Hr.objects.get(pk=validated_data.pop('hr_id'))
        return super().create(validated_data)


class SubUserUpdateAbstractSerializer(SubUserAbstractSerializer):
    def update(self, instance, validated_data):
        if validated_data.get('firstname') is not None:
            instance.user.firstname = validated_data.pop('firstname')
        if validated_data.get('lastname') is not None:
            instance.user.lastname = validated_data.pop('lastname')
        instance.user.save()
        return super().update(instance, validated_data)

    class Meta:
        abstract = True


class UpdateNewbieSerializer(SubUserUpdateAbstractSerializer):
    department = DepartmentSerializer(many=False, read_only=True)
    department_id = IntegerField(write_only=True)
    hr = HrRelatedSerializer(many=False, read_only=True)
    hr_id = IntegerField(write_only=True)

    class Meta:
        model = Newbie
        fields = ('firstname', 'lastname', 'user', 'department', 'position', 'hr', 'hr_id',
                  'department_id')

    def update(self, instance, validated_data):
        if validated_data.get('hr_id') is not None:
            instance.hr = Hr.objects.get(pk=validated_data.pop('hr_id'))
            instance.department = Department.objects.get(pk=validated_data.pop('department_id'))
        return super().update(instance, validated_data)


class UpdateHrSerializer(SubUserUpdateAbstractSerializer):
    class Meta:
        model = Hr
        fields = ('firstname', 'lastname', 'user')
