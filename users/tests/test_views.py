from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser, Newbie, Hr, Department
from users.serializers import HrSerializer, NewbieSerializer


class NewbieViewsTestCase(APITestCase):

    def test_create_newbie(self):
        department = Department.objects.create(head='test', place='test', name='test')
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123')
        hr = Hr.objects.create(user=user)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('create_newbie')
        data = {'email': 'test1@test.com',
                'password': 'Test123test123',
                'firstname': 'test',
                'lastname': 'test',
                'department_id': department.pk,
                'position': 'test',
                'hr_id': hr.pk}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.all().count(), 2)
        self.assertEqual(Newbie.objects.all().count(), 1)

    def test_update_newbie(self):
        department = Department.objects.create(head='test', place='test', name='test')
        department1 = Department.objects.create(head='test', place='test', name='test')
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123')
        user1 = CustomUser.objects.create_user(email='test1@test.com', password='Test123test123')
        user2 = CustomUser.objects.create_user(email='test2@test.com', password='Test123test123',
                                               firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)
        hr1 = Hr.objects.create(user=user1)
        newbie = Newbie.objects.create(user=user2, department=department, position='test', hr=hr)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('update_newbie', kwargs={'pk': newbie.pk})
        data = {
            'firstname': 'test1',
            'lastname': 'test1',
            'position': 'test1',
            'hr_id': hr1.pk,
            'department_id': department1.pk}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Newbie.objects.get().position, 'test1')
        self.assertEqual(Newbie.objects.get().hr, hr1)
        self.assertEqual(Newbie.objects.get().department, department1)
        self.assertEqual(Newbie.objects.get().user.firstname, 'test1')
        self.assertEqual(Newbie.objects.get().user.lastname, 'test1')


class HrViewsTestCase(APITestCase):
    def test_create_hr(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              is_staff=True)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('create_hr')
        data = {'email': 'test1@test.com',
                'password': 'Test123test123',
                'firstname': 'test',
                'lastname': 'test'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.all().count(), 2)
        self.assertEqual(Hr.objects.all().count(), 1)

    def test_update_hr(self):
        user = CustomUser.objects.create_superuser(email='test@test.com', password='Test123test123')
        user2 = CustomUser.objects.create_user(email='test2@test.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Hr.objects.create(user=user)
        hr = Hr.objects.create(user=user2)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('update_hr', kwargs={'pk': hr.pk})
        data = {
            'firstname': 'test1',
            'lastname': 'test1',
        }

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hr.objects.get(pk=hr.pk).user.firstname, 'test1')
        self.assertEqual(Hr.objects.get(pk=hr.pk).user.lastname, 'test1')


class UserViewsTestCase(APITestCase):
    def test_get_hr_data(self):
        user = CustomUser.objects.create_user(email='test2@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('get_user_data')

        response = self.client.get(url)
        data = HrSerializer(hr).data
        avatar = data['user'].pop('avatar')
        response_data = response.data
        response_avatar = response_data['user'].pop('avatar')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, data)
        self.assertIn(avatar, response_avatar)

    def test_get_newbie_data(self):
        user = CustomUser.objects.create_user(email='test2@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        newbie = Newbie.objects.create(user=user)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('get_user_data')

        response = self.client.get(url)
        data = NewbieSerializer(newbie).data
        avatar = data['user'].pop('avatar')
        response_data = response.data
        response_avatar = response_data['user'].pop('avatar')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, data)
        self.assertIn(avatar, response_avatar)

    def test_delete_hr(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123')
        user1 = CustomUser.objects.create_user(email='test2@test.com', password='Test123test123',
                                               firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)
        hr1 = Hr.objects.create(user=user1)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('delete_user', kwargs={'pk': user1.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hr.objects.all().count(), 1)
        self.assertEqual(CustomUser.objects.all().count(), 1)
        self.assertNotEquals(Hr.objects.get(), hr1)
        self.assertNotEquals(CustomUser.objects.get(), user1)

    def test_delete_newbie(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123')
        user1 = CustomUser.objects.create_user(email='test2@test.com', password='Test123test123',
                                               firstname='test', lastname='test')
        Hr.objects.create(user=user)
        Newbie.objects.create(user=user1)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('delete_user', kwargs={'pk': user1.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Newbie.objects.all().count(), 0)
        self.assertEqual(CustomUser.objects.all().count(), 1)
        self.assertNotEquals(CustomUser.objects.get(), user1)
