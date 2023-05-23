from django.urls import path

from .views import (ModuleListView, ManualListView, ManualCreateView,
                    ManualUpdateView, ManualDeleteView, ModuleCreateView,
                    ModuleUpdateView, ModuleDeleteView, AllModuleListView,
                    AllManualListView)

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
    path('tutorials/module/getall/', AllModuleListView.as_view(),
         name='get_all_modules'),
    path('tutorials/manual/getall/', AllManualListView.as_view(),
         name='get_all_modules')
]
