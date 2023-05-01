from rest_framework.test import APITestCase
from users.serializers import (DepartmentSerializer, UserSerializer, NewbieRelatedSerializer,
                               HrSerializer, HrRelatedSerializer, NewbieSerializer,
                               UpdateNewbieSerializer, UpdateHrSerializer)
from users.models import Department, CustomUser, Newbie, Hr


class DepartmentSerializerTestCase(APITestCase):
    def test_create_department(self):
        data = {'name': 'test',
                'head': 'test',
                'place': 'test'}
        serializer = DepartmentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data, data)
        self.assertEqual(Department.objects.all().count(), 1)
        self.assertEqual(Department.objects.get().name, 'test')
        self.assertEqual(Department.objects.get().head, 'test')
        self.assertEqual(Department.objects.get().place, 'test')

    def test_update_department(self):
        department = Department.objects.create(name='test', head='test', place='test')
        data = {'name': 'test1',
                'head': 'test1',
                'place': 'test1'}
        serializer = DepartmentSerializer(department, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(serializer.data, data)
        self.assertEqual(Department.objects.get().name, 'test1')
        self.assertEqual(Department.objects.get().head, 'test1')
        self.assertEqual(Department.objects.get().place, 'test1')

    def test_list_department(self):
        Department.objects.create(name='test', head='test', place='test')
        Department.objects.create(name='test1', head='test1', place='test1')

        data = [{'name': 'test', 'head': 'test', 'place': 'test'},
                {'name': 'test1', 'head': 'test1', 'place': 'test1'}]

        serializer = DepartmentSerializer(Department.objects.all(), many=True)
        self.assertEqual(serializer.data, data)

    def test_single_department(self):
        Department.objects.create(name='test', head='test', place='test')

        data = {'name': 'test', 'head': 'test', 'place': 'test'}

        serializer = DepartmentSerializer(Department.objects.get(), many=False)
        self.assertEqual(serializer.data, data)


class UserSerializerTestCase(APITestCase):
    def test_list_user(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        data = [{'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                 'lastname': user.lastname, 'avatar': user.avatar.url},
                {'pk': user1.pk, 'email': user1.email, 'firstname': user1.firstname,
                 'lastname': user1.lastname, 'avatar': user1.avatar.url}
                ]

        serializer = UserSerializer(CustomUser.objects.all(), many=True)
        self.assertEqual(serializer.data, data)

    def test_single_user(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        data = {'pk': user.pk,
                'email': user.email,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'avatar': user.avatar.url}

        serializer = UserSerializer(CustomUser.objects.get(), many=False)
        self.assertEqual(serializer.data, data)


class NewbieRelatedSerializerTestCase(APITestCase):
    def test_single_newbie(self):
        department = Department.objects.create(name='test', head='test', place='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        hr = Hr.objects.create(user=user1)
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        Newbie.objects.create(user=user, department=department, position='test', hr=hr)

        data = {'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                         'lastname': user.lastname, 'avatar': user.avatar.url},
                'department': {'name': 'test', 'head': 'test', 'place': 'test'},
                'position': 'test'}

        serializer = NewbieRelatedSerializer(Newbie.objects.get(), many=False)
        self.assertEqual(serializer.data, data)

    def test_list_newbie(self):
        department = Department.objects.create(name='test', head='test', place='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        hr = Hr.objects.create(user=user1)
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        Newbie.objects.create(user=user, department=department, position='test', hr=hr)
        user2 = CustomUser.objects.create_user(email='test2@test2.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Newbie.objects.create(user=user2, department=department, position='test', hr=hr)

        data = [{'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                          'lastname': user.lastname, 'avatar': user.avatar.url},
                 'department': {'name': 'test', 'head': 'test', 'place': 'test'},
                 'position': 'test'},
                {'user': {'pk': user2.pk, 'email': user2.email, 'firstname': user2.firstname,
                          'lastname': user2.lastname, 'avatar': user2.avatar.url},
                 'department': {'name': 'test', 'head': 'test', 'place': 'test'},
                 'position': 'test'}
                ]

        serializer = NewbieRelatedSerializer(Newbie.objects.all(), many=True)
        self.assertEqual(serializer.data, data)


class HrSerializerTestCase(APITestCase):
    def test_create_hr(self):
        data = {'email': 'test@test.com',
                'password': 'Test123test123',
                'firstname': 'test',
                'lastname': 'test'}
        serializer = HrSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(CustomUser.objects.all().count(), 1)
        self.assertEqual(Hr.objects.all().count(), 1)
        self.assertEqual(Hr.objects.get().user.email, 'test@test.com')
        self.assertEqual(Hr.objects.get().user.firstname, 'test')
        self.assertEqual(Hr.objects.get().user.lastname, 'test')

    def test_list_hr(self):
        user = CustomUser.objects.create_user(email='test@test1.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Hr.objects.create(user=user)
        Hr.objects.create(user=user1)

        data = [{'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                          'lastname': user.lastname, 'avatar': user.avatar.url},
                 'newbies': []},
                {'user': {'pk': user1.pk, 'email': user1.email, 'firstname': user1.firstname,
                          'lastname': user1.lastname, 'avatar': user1.avatar.url},
                 'newbies': []}]
        serializer = HrSerializer(Hr.objects.all(), many=True)
        self.assertEqual(serializer.data, data)

    def test_single_hr(self):
        user = CustomUser.objects.create_user(email='test@test1.com', password='Test123test123',
                                              firstname='test', lastname='test')
        Hr.objects.create(user=user)

        data = {'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                         'lastname': user.lastname, 'avatar': user.avatar.url},
                'newbies': []}

        serializer = HrSerializer(Hr.objects.get(), many=False)
        self.assertEqual(serializer.data, data)


class HrRelatedSerializerTestCase(APITestCase):
    def test_list_hr(self):
        user = CustomUser.objects.create_user(email='test@test1.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Hr.objects.create(user=user)
        Hr.objects.create(user=user1)

        data = [{'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                          'lastname': user.lastname, 'avatar': user.avatar.url}},
                {'user': {'pk': user1.pk, 'email': user1.email, 'firstname': user1.firstname,
                          'lastname': user1.lastname, 'avatar': user1.avatar.url}}]
        serializer = HrRelatedSerializer(Hr.objects.all(), many=True)
        self.assertEqual(serializer.data, data)

    def test_single_hr(self):
        user = CustomUser.objects.create_user(email='test@test1.com', password='Test123test123',
                                              firstname='test', lastname='test')
        Hr.objects.create(user=user)

        data = {'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                         'lastname': user.lastname, 'avatar': user.avatar.url}}

        serializer = HrRelatedSerializer(Hr.objects.get(), many=False)
        self.assertEqual(serializer.data, data)


class NewbieSerializerTestCase(APITestCase):
    def test_create_newbie(self):
        department = Department.objects.create(name='test', head='test', place='test')
        user = CustomUser.objects.create_user(email='test@test1.com', password='Test123test123')
        hr = Hr.objects.create(user=user)
        data = {'email': 'test@test.com',
                'password': 'Test123test123',
                'firstname': 'test',
                'lastname': 'test',
                'department_id': department.pk,
                'position': 'test',
                'hr_id': hr.pk}
        serializer = NewbieSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertEqual(CustomUser.objects.all().count(), 2)
        self.assertEqual(Newbie.objects.all().count(), 1)
        self.assertEqual(Newbie.objects.get().user.email, 'test@test.com')
        self.assertEqual(Newbie.objects.get().user.firstname, 'test')
        self.assertEqual(Newbie.objects.get().user.lastname, 'test')
        self.assertEqual(Newbie.objects.get().department, department)
        self.assertEqual(Newbie.objects.get().position, 'test')
        self.assertEqual(Newbie.objects.get().hr, hr)

    def test_list_newbie(self):
        department = Department.objects.create(name='test', head='test', place='test')
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        user2 = CustomUser.objects.create_user(email='test2@test2.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Newbie.objects.create(user=user1, department=department, position='test', hr=hr)
        Newbie.objects.create(user=user2, department=department, position='test', hr=hr)

        data = [
            {'user': {'pk': user1.pk, 'email': user1.email, 'firstname': user1.firstname,
                      'lastname': user1.lastname, 'avatar': user1.avatar.url},
             'department': {'name': 'test', 'head': 'test', 'place': 'test'},
             'position': 'test',
             'hr': {'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                             'lastname': user.lastname, 'avatar': user.avatar.url}}},
            {'user': {'pk': user2.pk, 'email': user2.email, 'firstname': user2.firstname,
                      'lastname': user2.lastname, 'avatar': user2.avatar.url},
             'department': {'name': 'test', 'head': 'test', 'place': 'test'},
             'position': 'test',
             'hr': {'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                             'lastname': user.lastname, 'avatar': user.avatar.url}}}
        ]
        serializer = NewbieSerializer(Newbie.objects.all(), many=True)
        self.assertEqual(serializer.data, data)

    def test_single_newbie(self):
        department = Department.objects.create(name='test', head='test', place='test')
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Newbie.objects.create(user=user1, department=department, position='test', hr=hr)

        data = {'user': {'pk': user1.pk, 'email': user1.email, 'firstname': user1.firstname,
                         'lastname': user1.lastname, 'avatar': user1.avatar.url},
                'department': {'name': 'test', 'head': 'test', 'place': 'test'},
                'position': 'test',
                'hr': {'user': {'pk': user.pk, 'email': user.email, 'firstname': user.firstname,
                                'lastname': user.lastname, 'avatar': user.avatar.url}}}
        serializer = NewbieSerializer(Newbie.objects.get(), many=False)
        self.assertEqual(serializer.data, data)


class UpdateNewbieSerializerTestCase(APITestCase):
    def test_update_newbie(self):
        department = Department.objects.create(name='test', head='test', place='test')
        department1 = Department.objects.create(name='test', head='test', place='test')
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        hr1 = Hr.objects.create(user=user1)
        user2 = CustomUser.objects.create_user(email='test2@test2.com', password='Test123test123',
                                               firstname='test', lastname='test')
        newbie = Newbie.objects.create(user=user2, department=department, position='test', hr=hr)

        data = {'firstname': 'test1',
                'lastname': 'test1',
                'department_id': department1.pk,
                'position': 'test1',
                'hr_id': hr1.pk}
        serializer = UpdateNewbieSerializer(newbie, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Newbie.objects.get().user.firstname, 'test1')
        self.assertEqual(Newbie.objects.get().user.lastname, 'test1')
        self.assertEqual(Newbie.objects.get().department, department1)
        self.assertEqual(Newbie.objects.get().position, 'test1')
        self.assertEqual(Newbie.objects.get().hr, hr1)


class UpdateHrSerializerTestCase(APITestCase):
    def test_update_hr(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)

        data = {'firstname': 'test1',
                'lastname': 'test1'}
        serializer = UpdateHrSerializer(hr, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Hr.objects.get().user.firstname, 'test1')
        self.assertEqual(Hr.objects.get().user.lastname, 'test1')
