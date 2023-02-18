from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Contact, CustomUser
from .serializers import ContactSerializer, UserSerializer

from Onboarding.settings import MEDIA_URL
class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()


class GetCurUserDataView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return user

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, *args, *kwargs)
        return Response(serializer.data)


class GetSuckersListView(ListModelMixin, GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_HR:
            HR_pk = self.request.user.pk

            users = CustomUser.objects.filter(HR_link=HR_pk)
            return users
        HR_pk = self.request.user.HR_link
        users = CustomUser.objects.filter(pk=HR_pk)
        return users

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
