from django.urls import path
from .views import ModuleListView,ManualListView,FileListView


urlpatterns = [
    path('tutorials/',ModuleListView.as_view()),
    path('tutorials/<int:module>',ManualListView.as_view()),
    path('tutorials/manual/<int:manual>',FileListView.as_view()),
]