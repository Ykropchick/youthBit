from django.urls import path


from .views import NotificationListView,NotificationDetailView,NotificationCreateView





urlpatterns = [
    path('notifications/',NotificationListView.as_view()),
    path('notifications/<int:pk>/',NotificationDetailView.as_view()),
    path('notifications/create/',NotificationCreateView.as_view()),
]