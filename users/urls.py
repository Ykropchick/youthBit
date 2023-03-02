from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
TokenRefreshView)

from .views import GetCurUserDataView,CreateNewbieView,CreateHrView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/',GetCurUserDataView.as_view()),
    path('hr/register/',CreateHrView.as_view()),
    path('newbie/register/',CreateNewbieView.as_view())
]