from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ModuleListSerializer,ManualListSerializer,FileListSerializer
from .models import Module,Manual,File


class ModuleListView(ListModelMixin,GenericAPIView):
    serializer_class = ModuleListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        department = self.request.user.department
        modules = Module.objects.filter(department=department)
        return modules

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class ManualListView(ListModelMixin,GenericAPIView):
    serializer_class = ManualListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        module = self.kwargs['module']
        manuals = Manual.objects.filter(module=module)
        return manuals

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class FileListView(ListModelMixin,GenericAPIView):
    serializer_class = FileListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        manual = self.kwargs['manual']
        files = File.objects.filter(manual=manual)
        return files

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)