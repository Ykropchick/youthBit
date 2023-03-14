from django.db import models

from users.models import Department
from .managers import ModuleManager, ManualManager


class Module(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField('Описание', max_length=300, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   null=True, verbose_name='Отдел')

    objects = ModuleManager()


class Manual(models.Model):
    name = models.CharField('Название', max_length=60)
    description = models.CharField('Описание', max_length=200)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='Модуль')
    file = models.FileField('Файл', upload_to="manuals")

    objects = ManualManager()
