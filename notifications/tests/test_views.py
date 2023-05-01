from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser
from notifications.models import Notification
from notifications.serializers import NotificationSerializer


class NotificationsViewsTestCase(APITestCase):
    def test_create_notification(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('create_notification')
        data = {'title': 'test',
                'description': 'test',
                'to_id': user.pk,
                'sender_id': user1.pk}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notification.objects.all().count(), 1)

    def test_update_notification(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        notification = Notification.objects.create(title='test', description='test',
                                                   to=user, sender=user1)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('update_notification', kwargs={'pk': notification.pk})
        data = {'title': 'test1',
                'description': 'test1',
                'to_id': user1.pk,
                'sender_id': user.pk}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Notification.objects.get().title, 'test1')
        self.assertEqual(Notification.objects.get().description, 'test1')
        self.assertEqual(Notification.objects.get().to, user1)
        self.assertEqual(Notification.objects.get().sender, user)

    def test_list_notifications(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        user1 = CustomUser.objects.create_user(email='test1@test1.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Notification.objects.create(title='test', description='test',
                                    to=user, sender=user1)
        Notification.objects.create(title='test', description='test',
                                    to=user, sender=user1)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('get_list_notifications')

        serializer = NotificationSerializer(Notification.objects.all(), many=True)

        response = self.client.get(url)

        self.assertEqual(response.data, serializer.data)
