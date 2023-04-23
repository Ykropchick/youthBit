from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.files.uploadedfile import SimpleUploadedFile

from welcomejorney.models import Module,Manual
from users.models import Department, CustomUser, Hr


class ModuleTestCase(APITestCase):
    def test_create_module(self):
        url = reverse('create_module')
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        data = {'department': department.pk,
                'name': 'test',
                'description': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Module.objects.all().count(), 1)
        self.assertEqual(Module.objects.get().name, 'test')

    def test_update_module(self):
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        module = Module.objects.create(department=department, name='test', description='test')

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('update_module', kwargs={'pk': module.pk})
        data = {'department': department.pk,
                'name': 'test1',
                'description': 'test1'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Module.objects.get(pk=module.pk).name, 'test1')
        self.assertEqual(Module.objects.get(pk=module.pk).description, 'test1')

    def test_update_module_partial(self):
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        module = Module.objects.create(department=department, name='test', description='test')

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('update_module', kwargs={'pk': module.pk})
        data = {'name': 'test1'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Module.objects.get(pk=module.pk).name, 'test1')

    def test_delete_module(self):
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        module = Module.objects.create(department=department, name='test', description='test')

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('delete_module', kwargs={'pk': module.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Module.objects.all().count(), 0)

    def test_list_module(self):
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        Module.objects.create(department=department, name='test', description='test')

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('get_modules_by_department', kwargs={'department': department.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ManualTestCase(APITestCase):
    def test_manual_create(self):
        url = reverse('create_manual')
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        module = Module.objects.create(name='test', description='test',
                                       department=department)
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        file = SimpleUploadedFile('file.html', b'file_content', 'text/plain')

        data = {'module': module.pk,
                'name': 'test',
                'description': 'test',
                'file': file}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Manual.objects.all().count(), 1)
        self.assertEqual(Manual.objects.get().name, 'test')

    def test_update_manual(self):
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        module = Module.objects.create(department=department, name='test', description='test')

        file1 = SimpleUploadedFile('test.html', b'file_content', content_type='text/plain')
        file2 = SimpleUploadedFile('test1.html', b'file_content', content_type='text/plain')
        manual = Manual.objects.create(module=module, name='test', description='test', file=file1)

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('update_manual', kwargs={'pk': manual.pk})
        data = {'module': module.pk,
                'name': 'test1',
                'description': 'test1',
                'file': file2}
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Manual.objects.get(pk=manual.pk).name, 'test1')
        self.assertEqual(Manual.objects.get(pk=manual.pk).description, 'test1')
        self.assertIn('test1',Manual.objects.get().file.name)

    def test_update_manual_partial(self):
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        module = Module.objects.create(department=department, name='test', description='test')

        file1 = SimpleUploadedFile('test.html', b'file_content', content_type='text/plain')
        manual = Manual.objects.create(module=module, name='test', description='test', file=file1)

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('update_manual', kwargs={'pk': manual.pk})
        data = {'name': 'test1'}
        response = self.client.patch(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Manual.objects.get(pk=manual.pk).name, 'test1')

    def test_delete_manual(self):
        department = Department.objects.create(name='Test', head='Test',
                                               place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                              password='Test1234test9876', )
        module = Module.objects.create(department=department, name='test', description='test')

        file1 = SimpleUploadedFile('test.html', b'file_content', content_type='text/plain')
        manual = Manual.objects.create(module=module, name='test', description='test', file=file1)

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('delete_manual', kwargs={'pk': manual.pk})
        response = self.client.delete(url, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Manual.objects.all().count(),0)

    def test_list_module(self):
        department = Department.objects.create(name='Test', head='Test',
                                                   place='Test')
        user = CustomUser.objects.create_user(email='admin@admin.ru',
                                                  password='Test1234test9876', )
        module = Module.objects.create(department=department, name='test', description='test')

        file1 = SimpleUploadedFile('test.html', b'file_content', content_type='text/plain')
        Manual.objects.create(module=module, name='test', description='test', file=file1)

        Hr.objects.create(user=user)
        token = RefreshToken.for_user(user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(token)}')

        url = reverse('get_manual_by_module', kwargs={'module': module.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)