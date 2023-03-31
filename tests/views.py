from django.http import HttpResponse
from rest_framework.generics import GenericAPIView

from users.models import Department
from django.contrib.auth import get_user_model
from random import randint,choice

class FillView(GenericAPIView):
    def get(self,*args,**kwargs):
        department = Department.objects.create(name='testdep', head='test_head',
place='zalupa')

        users = []
        user_model = get_user_model()
        start_id = max(user.pk for user in user_model.objects.all())
        for i in range(start_id+1,start_id+11):
            email = f'test{i}@test.com'
            password = 'Qwerty123321'
            firstname = 'test'
            lastname = 'user'
            is_HR = randint(0, 1)
            HR_link = None
            if not is_HR:
                HR_link = choice(user_model.objects.filter(is_HR=True)).pk

            user_model.objects.create_user(email=email,
                                           password=password, firstname=firstname, lastname=lastname,HR_link=HR_link, is_HR=is_HR)

        return HttpResponse("Готово")