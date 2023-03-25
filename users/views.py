from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   UpdateModelMixin)

from .permissions import IsHRUserOrReadOnly
from .serializers import (NewbieSerializer, HrSerializer,
                          UpdateNewbieSerializer, UserSerializer,
                          UpdateHrSerializer)
from .models import Hr, Newbie, CustomUser


class GetCurUserDataView(GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        if Hr.objects.is_user_hr(self.request.user):
            self.serializer_class = HrSerializer
            hr = Hr.objects.get_subobject_byuser(self.request.user)
            return hr
        self.serializer_class = NewbieSerializer
        newbie = Newbie.objects.get_subobject_byuser(self.request.user)
        return newbie

    def get(self, request, *args, **kwargs):

        sub_user_object = self.get_object()
        serializer = self.get_serializer(sub_user_object, many=False)
        return Response(serializer.data)


class DeleteUserView(DestroyModelMixin, GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsHRUserOrReadOnly,)

    def get_queryset(self):
        return CustomUser.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateNewbieView(CreateModelMixin, GenericAPIView):
    serializer_class = NewbieSerializer
    permission_classes = (IsHRUserOrReadOnly, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        cur_hr = Hr.objects.get_subobject_byuser(self.request.user.id)
        serializer.save(hr=cur_hr)


class UpdateNewbieView(UpdateModelMixin, GenericAPIView):
    serializer_class = UpdateNewbieSerializer
    permission_classes = (IsHRUserOrReadOnly, )

    def get_queryset(self):
        return Newbie.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CreateHrView(CreateModelMixin, GenericAPIView):
    serializer_class = HrSerializer
    permission_classes = (IsAdminUser, )

    def post(self, request):
        return self.create(request)


class UpdateHrView(UpdateModelMixin, GenericAPIView):
    serializer_class = UpdateHrSerializer
    permission_classes = (IsHRUserOrReadOnly, )

    def get_queryset(self):
        return Hr.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
