from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser, Newbie, Hr, Department


class NewbieViewsTestCase(APITestCase):

    def create_newbie_test(self):
        department = Department.objects.create(head='test',place='test',name='test')
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123')
        hr = Hr.objects.create(user=user)

        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('create_module')
        data = {'email': 'test@test.com',
                'password': 'Test123test123',
                'firstname': 'test',
                'lastname': 'test',
                'department': department.pk,
                'position': 'test',
                'hr': hr.pk}

        response = self.client.post(url,data,content_type='json')
        print(response.data)

