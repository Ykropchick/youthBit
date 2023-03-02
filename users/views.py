from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from .permissions import IsHRUserOrReadOnly
from .serializers import NewbieSerializer,HrSerializer
from .models import Hr,Newbie


class GetCurUserDataView(GenericAPIView,ListModelMixin):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if Hr.objects.is_user_hr(self.request.user):
            self.serializer_class = HrSerializer
            return Hr.objects.get_subobject_byuser(self.request.user)
        self.serializer_class = NewbieSerializer
        return Newbie.objects.get_subobject_byuser(self.request.user)

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,*args,*kwargs)
        return Response(serializer.data)


class CreateNewbieView(CreateModelMixin,GenericAPIView):
    serializer_class = NewbieSerializer
    permission_classes = (IsHRUserOrReadOnly,)

    def post(self,request):
        return self.create(request)

    def perform_create(self, serializer):
        cur_HR = Hr.objects.get_subobject_byuser(self.request.user.id)
        new_Newbie = serializer.save()
        cur_HR.newbies.add(new_Newbie)
        cur_HR.save()


class CreateHrView(CreateModelMixin,GenericAPIView):
    serializer_class = HrSerializer
    permission_classes = (IsAdminUser,)

    def post(self,request):
        return self.create(request)