from io import BytesIO

from PIL.Image import open
from django.contrib.auth.models import BaseUserManager
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from Onboarding.settings import MEDIA_ROOT, MEDIA_URL
from utils import create_avatar


def resize_image(image_field, width=512, height=512, name=None):
    """
    Resizes an image from a Model.ImageField and returns a new image as a ContentFile
    """
    img = open(image_field)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
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

    def create_superuser(self, email, password=None, **kwargs):
        email = self.normalize_email(email)

        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user
