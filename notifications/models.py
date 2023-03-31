from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Notification(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    description = models.CharField('Описание', max_length=100)
    date = models.DateTimeField('Дата создания', auto_now=True)
    is_read = models.BooleanField(default=False)
    to = models.ForeignKey(user, on_delete=models.CASCADE,
                           verbose_name='Адресат', related_name="to")
    sender = models.ForeignKey(user, on_delete=models.CASCADE,
                               verbose_name='Адресант', related_name='sender')
