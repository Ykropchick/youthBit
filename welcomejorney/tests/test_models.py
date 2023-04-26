from rest_framework.test import APITestCase

from welcomejorney.models import Module, Manual
from users.models import Department


class ManualManagerTestCase(APITestCase):
    def test_get_single_manual_by_module(self):
        department = Department.objects.create(name='test', head='test', place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        manual = Manual.objects.create(name='test', description='test', module=module)

        get_manual = Manual.objects.get_manuals_bymodule(module=module)

        self.assertEqual(get_manual[0], manual)

    def test_get_list_manual_by_module(self):
        department = Department.objects.create(name='test', head='test', place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        manual = Manual.objects.create(name='test', description='test', module=module)
        manual1 = Manual.objects.create(name='test', description='test', module=module)

        get_manual = Manual.objects.get_manuals_bymodule(module=module)

        self.assertEqual(get_manual[0], manual)
        self.assertEqual(get_manual[1], manual1)


class ModuleManagerTestCase(APITestCase):
    def test_get_single_module_by_department(self):
        department = Department.objects.create(name='test', head='test', place='test')
        module = Module.objects.create(name='test', description='test', department=department)

        get_module = Module.objects.get_module_bydepartment(department=department)

        self.assertEqual(get_module[0], module)

    def test_get_list_module_by_department(self):
        department = Department.objects.create(name='test', head='test', place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        module1 = Module.objects.create(name='test', description='test', department=department)

        get_module = Module.objects.get_module_bydepartment(department=department)

        self.assertEqual(get_module[0], module)
        self.assertEqual(get_module[1], module1)
