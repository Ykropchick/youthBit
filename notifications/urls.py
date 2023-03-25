from django.urls import path


from .views import (NotificationListView, NotificationCreateView,
                    NotificationUpdateStatusView)


urlpatterns = [
    path('notifications/', NotificationListView.as_view()),
    path('notifications/update/<int:pk>/', NotificationUpdateStatusView.as_view()),
    path('notifications/create/', NotificationCreateView.as_view()),
]
