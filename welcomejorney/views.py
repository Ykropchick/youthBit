from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin,
                                   CreateModelMixin, UpdateModelMixin,
                                   DestroyModelMixin)
from rest_framework.permissions import IsAuthenticated

from .models import Module, Manual
from .serializers import ModuleSerializer, ManualSerializer
from users.permissions import IsHRUserOrReadOnly


class ModuleListView(ListModelMixin, GenericAPIView):
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        department = self.kwargs['department']
        return Module.objects.get_module_bydepartment(department)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ModuleCreateView(CreateModelMixin, GenericAPIView):
    serializer_class = ModuleSerializer
    permission_classes = (IsHRUserOrReadOnly, )

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)


class ModuleUpdateView(UpdateModelMixin, GenericAPIView):
    serializer_class = ModuleSerializer
    permission_classes = (IsHRUserOrReadOnly, )
    queryset = Module.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ModuleDeleteView(DestroyModelMixin, GenericAPIView):
    serializer_class = ModuleSerializer
    permission_classes = (IsHRUserOrReadOnly, )
    queryset = Module.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ManualListView(ListModelMixin, GenericAPIView):
    serializer_class = ManualSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        module = self.kwargs['module']
        return Manual.objects.get_manuals_bymodule(module)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ManualCreateView(CreateModelMixin, GenericAPIView):
    serializer_class = ManualSerializer
    permission_classes = (IsHRUserOrReadOnly, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ManualUpdateView(UpdateModelMixin, GenericAPIView):
    serializer_class = ManualSerializer
    permission_classes = (IsHRUserOrReadOnly, )
    queryset = Manual.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ManualDeleteView(DestroyModelMixin, GenericAPIView):
    serializer_class = ManualSerializer
    permission_classes = (IsHRUserOrReadOnly, )
    queryset = Manual.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
