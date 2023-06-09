from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, CustomTokenObtainPairView, RefreshTokenView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/token/refresh/', RefreshTokenView.as_view(), name='token_refresh')
]
