from django.urls import path

from .views import (ModuleListView, ManualListView, ManualDetailView,
                    ManualCreateView, ManualUpdateView, ManualDeleteView,
                    ModuleCreateView, ModuleUpdateView, ModuleDeleteView)

urlpatterns = [
    path('tutorials/module/<int:department>/', ModuleListView.as_view()),
    path('tutorials/module/create/', ModuleCreateView.as_view()),
    path('tutorials/module/update/<int:pk>/', ModuleUpdateView.as_view()),
    path('tutorials/module/delete/<int:pk>/', ModuleDeleteView.as_view()),
    path('tutorials/manual/<int:module>/', ManualListView.as_view()),
    path('tutorials/manual/detail/<int:pk>/', ManualDetailView.as_view()),
    path('tutorials/manual/create/', ManualCreateView.as_view()),
    path('tutorials/manual/update/<int:pk>/', ManualUpdateView.as_view()),
    path('tutorials/manual/delete/<int:pk>/', ManualDeleteView.as_view()),
]
