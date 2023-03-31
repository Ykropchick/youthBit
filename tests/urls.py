from django.urls import path
from .views import FillView

urlpatterns = [
    path('fill/',FillView.as_view())
]