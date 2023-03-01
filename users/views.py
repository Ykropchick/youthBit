from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from welcomejorney.permissions import IsHRUserOrReadOnly
from .serializers import UserSerializer,NewbieSerializer,HrSerializer
from .models import CustomUser,Hr,Newbie


class GetCurUserDataView(GenericAPIView,ListModelMixin):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        hr_user = Hr.objects.get_hr_by_user(self.request.user)
        if not isinstance(hr_user,str):
            self.serializer_class = HrSerializer
            return hr_user
        newbie_user = Newbie.objects.get_newbie_by_user(self.request.user)
        if not isinstance(newbie_user,str):
            self.serializer_class = NewbieSerializer
            return newbie_user


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
        cur_HR = Hr.objects.get_hr_by_user(self.request.user.id)
        new_Newbie = serializer.save()
        if not isinstance(cur_HR,str):
            cur_HR.newbies.add(new_Newbie)
            cur_HR.save()
class CreateHrView(CreateModelMixin,GenericAPIView):
    serializer_class = HrSerializer
    permission_classes = (IsAdminUser,)

    def post(self,request):
        return self.create(request)