from rest_framework.test import APITestCase
from rest_framework.serializers import DateTimeField

from notifications.models import Notification
from notifications.serializers import CustomUserInfoSerializer, NotificationSerializer
from users.models import CustomUser


class CustomUserInfoSerializerTestCase(APITestCase):
    def test_list_user(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')

        data = [{'pk': user.pk, 'firstname': user.firstname, 'lastname': user.lastname},
                {'pk': user1.pk, 'firstname': user1.firstname, 'lastname': user1.lastname}]

        serializer = CustomUserInfoSerializer(CustomUser.objects.all(), many=True)

        self.assertEqual(serializer.data, data)

    def test_single_user(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')

        data = {'pk': user.pk, 'firstname': user.firstname, 'lastname': user.lastname}

        serializer = CustomUserInfoSerializer(CustomUser.objects.get(), many=False)

        self.assertEqual(serializer.data, data)


class NotificationSerializerTestCase(APITestCase):
    def test_create_notification(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')

        data = {'title': 'test',
                'description': 'test',
                'to_id': user.pk,
                'sender_id': user1.pk}

        serializer = NotificationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Notification.objects.get().title, 'test')
        self.assertEqual(Notification.objects.get().description, 'test')
        self.assertEqual(Notification.objects.get().to, user)
        self.assertEqual(Notification.objects.get().sender, user1)

    def test_update_notification(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        notification = Notification.objects.create(title='test', description='test', to=user, sender=user1)

        data = {'title': 'test1',
                'description': 'test1',
                'to_id': user1.pk,
                'sender_id': user.pk,
                'is_read': True}

        serializer = NotificationSerializer(notification, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Notification.objects.get().title, 'test1')
        self.assertEqual(Notification.objects.get().description, 'test1')
        self.assertEqual(Notification.objects.get().to, user1)
        self.assertEqual(Notification.objects.get().sender, user)
        self.assertTrue(Notification.objects.get().is_read)

    def test_list_notifications(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        notification = Notification.objects.create(title='test', description='test', to=user, sender=user1)
        notification1 = Notification.objects.create(title='test', description='test', to=user, sender=user1)

        date = DateTimeField().to_representation(notification.date)
        date1 = DateTimeField().to_representation(notification1.date)

        data = [{'pk': notification.pk,
                 'title': notification.title,
                 'description': notification.description,
                 'to': {'pk': user.pk, 'firstname': user.firstname, 'lastname': user.lastname},
                 'sender': {'pk': user1.pk, 'firstname': user1.firstname,
                            'lastname': user1.lastname},
                 'date': date,
                 'is_read': False},

                {'pk': notification1.pk,
                 'title': notification1.title,
                 'description': notification1.description,
                 'to': {'pk': user.pk, 'firstname': user.firstname, 'lastname': user.lastname},
                 'sender': {'pk': user1.pk, 'firstname': user1.firstname,
                            'lastname': user1.lastname},
                 'date': date1,
                 'is_read': False}]

        serializer = NotificationSerializer(Notification.objects.all(), many=True)

        self.assertEqual(serializer.data, data)

    def test_single_notification(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        notification = Notification.objects.create(title='test', description='test', to=user, sender=user1)

        date = DateTimeField().to_representation(notification.date)

        data = {'pk': notification.pk,
                'title': notification.title,
                'description': notification.description,
                'to': {'pk': user.pk, 'firstname': user.firstname, 'lastname': user.lastname},
                'sender': {'pk': user1.pk, 'firstname': user1.firstname,
                           'lastname': user1.lastname},
                'date': date,
                'is_read': False}

        serializer = NotificationSerializer(Notification.objects.get(), many=False)

        self.assertEqual(serializer.data, data)
