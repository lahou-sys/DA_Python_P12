from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import APILogoutView


urlpatterns = [
    path('auth-token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', APILogoutView.as_view(), name='logout_token'),
]