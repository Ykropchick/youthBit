from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (ModuleViewSet,ManualViewSet,ModuleByDepartmentView,\
ManualByModuleView)

router = DefaultRouter()
router.register(r'modules',ModuleViewSet,basename='module')
router.register(r'manuals',ManualViewSet,basename='manual')

urlpatterns = [
    path('',include(router.urls)),
    path('modules/bydep/<int:department>',ModuleByDepartmentView.as_view()),
    path('manuals/bymod/<int:module>',ManualByModuleView.as_view())
]