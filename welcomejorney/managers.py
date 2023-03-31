from django.db.models import Manager


class ManualManager(Manager):

    def get_manuals_bymodule(self, module):
        return self.get_queryset().filter(module=module)


class ModuleManager(Manager):

    def get_module_bydepartment(self, department):
        return self.get_queryset().filter(department=department)
