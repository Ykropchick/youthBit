from django.urls import path


from .views import (NotificationListView, NotificationCreateView,
                    NotificationUpdateView)


urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='get_list_notifications'),
    path('notifications/update/<int:pk>/', NotificationUpdateView.as_view(),
         name='update_notification'),
    path('notifications/create/', NotificationCreateView.as_view(), name='create_notification'),
]
