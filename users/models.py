from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager


class Department(models.Model):
    name = models.CharField('Название',max_length=100)
    head = models.CharField('Имя главы', max_length=40)
    place = models.CharField('Местоположение',max_length=150,null=True)


class CustomUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField('Электронная почта',unique=True)
    firstname = models.CharField('Имя',max_length=30)
    lastname = models.CharField('Фамилия',max_length=30)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,
null=True,verbose_name='Отдел')
    is_HR = models.BooleanField('Сотрудник HR',default=False)
    HR_link = models.BigIntegerField('Курирующий HR',null=True,unique=False)
    start_date = models.DateField('Дата начала работы',auto_now=True)
    is_started = models.BooleanField('Зашёл ли сотрудник на портал',
default=False)
    position = models.CharField('Должность',max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()


class Contact(models.Model):
    telegram = models.CharField('Телеграмм',max_length=50)
    phone_number = models.CharField('Номер телефона',max_length=13)
    user = models.ForeignKey(CustomUser,models.CASCADE,verbose_name='Владелец')
