from django.urls import path

from .views import (ModuleListView, ManualListView, ManualCreateView,
                    ManualUpdateView, ManualDeleteView, ModuleCreateView,
                    ModuleUpdateView, ModuleDeleteView)

urlpatterns = [
    path('tutorials/module/<int:department>/', ModuleListView.as_view(),
         name='get_modules_by_department'),
    path('tutorials/module/create/', ModuleCreateView.as_view(),
         name='create_module'),
    path('tutorials/module/update/<int:pk>/', ModuleUpdateView.as_view(),
         name='update_module'),
    path('tutorials/module/delete/<int:pk>/', ModuleDeleteView.as_view(),
         name='delete_module'),
    path('tutorials/manual/<int:module>/', ManualListView.as_view(),
         name='get_manual_by_module'),
    path('tutorials/manual/create/', ManualCreateView.as_view(),
         name='create_manual'),
    path('tutorials/manual/update/<int:pk>/', ManualUpdateView.as_view(),
         name='update_manual'),
    path('tutorials/manual/delete/<int:pk>/', ManualDeleteView.as_view(),
         name='delete_manual'),
]
