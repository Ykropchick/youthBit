from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ModuleSerializer, ManualSerializer
from .permissions import IsHRUserOrReadOnly
from .models import Module,Manual


class ModuleViewSet(ModelViewSet):
    serializer_class = ModuleSerializer
    permission_classes = (IsHRUserOrReadOnly,)
    queryset = Module.objects.all()



class ModuleByDepartmentView(GenericAPIView,ListModelMixin):
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        department = self.kwargs['department']
        modules = Module.objects.filter(department=department)
        return modules

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)



class ManualViewSet(ModelViewSet):
    serializer_class = ManualSerializer
    permission_classes = (IsHRUserOrReadOnly,)
    queryset = Manual.objects.all()



class ManualByModuleView(GenericAPIView,ListModelMixin):
    serializer_class = ManualSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        module = self.kwargs['module']
        manuals = Manual.objects.filter(module=module)
        return manuals

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)