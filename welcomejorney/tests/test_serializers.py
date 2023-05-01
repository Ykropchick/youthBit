from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from welcomejorney.serializers import ModuleSerializer, ManualSerializer
from users.models import Department
from welcomejorney.models import Module, Manual


class ModuleSerializerTestCase(APITestCase):
    def test_create_module(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        data = {'name': 'test',
                'description': 'test',
                'department': department.pk}
        serializer = ModuleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Module.objects.all().count(), 1)
        self.assertEqual(Module.objects.get().name, 'test')
        self.assertEqual(Module.objects.get().description, 'test')
        self.assertEqual(Module.objects.get().department, department)

    def test_update_module(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        data = {'name': 'test1',
                'description': 'test1',
                'department': department.pk}
        serializer = ModuleSerializer(module, data=data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Module.objects.get().name, 'test1')
        self.assertEqual(Module.objects.get().description, 'test1')
        self.assertEqual(Module.objects.get().department, department)

    def test_update_module_partial(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        data = {'name': 'test1'}
        serializer = ModuleSerializer(module, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Module.objects.get().name, 'test1')
        self.assertEqual(Module.objects.get().description, 'test')
        self.assertEqual(Module.objects.get().department, department)

    def test_list_module(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        module1 = Module.objects.create(name='test', description='test', department=department)
        data = [{'pk': module.pk, 'department': department.pk, 'name': module.name,
                 'description': module.description},
                {'pk': module1.pk, 'department': department.pk, 'name': module1.name,
                 'description': module1.description}]
        queryset = Module.objects.all()
        serializer = ModuleSerializer(queryset, many=True)
        self.assertEqual(serializer.data, data)

    def test_single_module(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        data = {'pk': module.pk, 'department': department.pk, 'name': module.name,
                'description': module.description}
        serializer = ModuleSerializer(module, many=False)
        self.assertEqual(serializer.data, data)


class ManualSerializerTestCase(APITestCase):
    def test_create_manual(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        file = SimpleUploadedFile('test.html', b'file_content', 'plain/text')
        data = {'name': 'test',
                'description': 'test',
                'module': module.pk,
                'file': file}
        serializer = ManualSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Manual.objects.all().count(), 1)
        self.assertEqual(Manual.objects.get().name, 'test')
        self.assertEqual(Manual.objects.get().description, 'test')
        self.assertEqual(Manual.objects.get().module, module)
        self.assertIn('test', Manual.objects.get().file.name)

    def test_update_manual(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        file = SimpleUploadedFile('test.html', b'file_content', 'plain/text')
        file1 = SimpleUploadedFile('test1.html', b'file_content', 'plain/text')
        manual = Manual.objects.create(name='test', description='test', module=module, file=file)
        data = {'name': 'test1',
                'description': 'test1',
                'module': module.pk,
                'file': file1}
        serializer = ManualSerializer(manual, data=data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Manual.objects.get().name, 'test1')
        self.assertEqual(Manual.objects.get().description, 'test1')
        self.assertEqual(Manual.objects.get().module, module)
        self.assertIn('test1', Manual.objects.get().file.name)

    def test_update_manual_partial(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        file = SimpleUploadedFile('test.html', b'file_content', 'plain/text')
        manual = Manual.objects.create(name='test', description='test', module=module, file=file)
        data = {'name': 'test1'}
        serializer = ManualSerializer(manual, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Manual.objects.get().name, 'test1')

    def test_list_manual(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        file = SimpleUploadedFile('test.html', b'file_content', 'plain/text')
        manual = Manual.objects.create(name='test', description='test', module=module, file=file)
        manual1 = Manual.objects.create(name='test', description='test', module=module, file=file)

        data = [{'pk': manual.pk, 'module': module.pk, 'name': manual.name,
                 'description': manual.description, 'file': manual.file.url},
                {'pk': manual1.pk, 'module': module.pk, 'name': manual1.name,
                 'description': manual1.description, 'file': manual1.file.url}]
        queryset = Manual.objects.all()
        serializer = ManualSerializer(queryset, many=True)
        self.assertEqual(serializer.data, data)

    def test_single_module(self):
        department = Department.objects.create(name='test', head='test',
                                               place='test')
        module = Module.objects.create(name='test', description='test', department=department)
        file = SimpleUploadedFile('test.html', b'file_content', 'plain/text')
        manual = Manual.objects.create(name='test', description='test', module=module, file=file)
        data = {'pk': manual.pk, 'module': module.pk, 'name': manual.name,
                'description': manual.description,
                'file': manual.file.url}
        serializer = ManualSerializer(manual, many=False)
        self.assertEqual(serializer.data, data)
