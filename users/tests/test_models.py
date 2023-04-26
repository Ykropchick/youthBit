from rest_framework.test import APITestCase

from users.models import CustomUser, Hr, Newbie


class CustomUserManagerTestCase(APITestCase):
    def test_create_user(self):
        CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                       firstname='test', lastname='test')

        self.assertEqual(CustomUser.objects.get().email, 'test@test.com')
        self.assertEqual(CustomUser.objects.get().firstname, 'test')
        self.assertEqual(CustomUser.objects.get().lastname, 'test')
        self.assertNotEquals(CustomUser.objects.get().password, None)
        self.assertNotEquals(CustomUser.objects.get().avatar, None)

    def test_create_superuser(self):
        CustomUser.objects.create_superuser(email='test@test.com', password='Test123test123',
                                            firstname='test', lastname='test')

        self.assertEqual(CustomUser.objects.get().email, 'test@test.com')
        self.assertEqual(CustomUser.objects.get().firstname, 'test')
        self.assertEqual(CustomUser.objects.get().lastname, 'test')
        self.assertEqual(CustomUser.objects.get().is_staff, True)
        self.assertEqual(CustomUser.objects.get().is_superuser, True)
        self.assertNotEquals(CustomUser.objects.get().password, None)
        self.assertNotEquals(CustomUser.objects.get().avatar, None)


class HrManagerTestCase(APITestCase):
    def test_get_hr_by_user(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)
        get_hr = Hr.objects.get_subobject_byuser(user=user)

        self.assertEqual(get_hr,hr)

    def test_is_user_hr_success(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        hr = Hr.objects.create(user=user)
        is_hr = Hr.objects.is_user_hr(user=user)

        self.assertTrue(is_hr)

    def test_is_user_hr_fail(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        is_hr = Hr.objects.is_user_hr(user=user)

        self.assertFalse(is_hr)


class NewbieManagerTestCase(APITestCase):
    def test_get_newbie_by_user(self):
        user = CustomUser.objects.create_user(email='test@test.com', password='Test123test123',
                                              firstname='test', lastname='test')
        newbie = Newbie.objects.create(user=user)
        get_newbie = Newbie.objects.get_subobject_byuser(user=user)

        self.assertEqual(get_newbie, newbie)
