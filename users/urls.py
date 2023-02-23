from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
TokenRefreshView)

from .views import GetCurUserDataView,GetSuckersListView,CreateUserView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/',GetCurUserDataView.as_view()),
    path('me/suckers/',GetSuckersListView.as_view()),
    path('register/',CreateUserView.as_view())

]