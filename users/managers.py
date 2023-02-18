from django.contrib.auth.models import BaseUserManager
from utils import create_avatar

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        im = create_avatar()
        image_field = user.image_field
        img_name = f'avatar{user.id}.jpg'
        img_path = settings.MEDIA_ROOT + img_name

        pillow_image = resize_image(
            image_field,
            width=IMAGE_WIDTH,
            height=IMAGE_HEIGHT,
            name=img_path)

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
