from io import BytesIO

from django.contrib.auth.models import BaseUserManager
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ObjectDoesNotExist
from django.db import models



from Onboarding.settings import MEDIA_ROOT, MEDIA_URL
from utils import create_avatar



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None,*args, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email,*args,**kwargs)
        user.set_password(password)
        user.save()

        img = create_avatar()
        image_field = user.avatar
        img_name = f'avatar{user.id}.jpg'
        img_path = MEDIA_URL / MEDIA_ROOT / img_name

        buffer = BytesIO()
        img.save(fp=buffer, format='PNG')
        pillow_image = ContentFile(buffer.getvalue())

        image_field.save(img_name, InMemoryUploadedFile(
            pillow_image,  # file
            None,  # field_name
            img_name,  # file name
            'image/jpeg',  # content_type
            pillow_image.tell,  # size
            None)  # content_type_extra
                         )
        return user

    def create_superuser(self, email, password=None,*args,**kwargs):

        return self.create_user(email,password,is_staff=True,is_superuser=True,*args,**kwargs)


class HrManager(models.Manager):

    def get_hr_by_user(self,user):
        try:
            hr = super().get_queryset().get(user=user)
            return hr
        except ObjectDoesNotExist:
            return 'Not found'


class NewbieManager(models.Manager):

    def get_newbie_by_user(self,user):
        try:
            newbie = super().get_queryset().get(user=user)
            return newbie
        except ObjectDoesNotExist:
            return 'Not found'





