from django.urls import path
from Auth.views import (
    UserRegisterationView,
    UserLoginView,
    UserProfileView,
    UserChangePasswordView
)

urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name="Registeration"),
    path('login/', UserLoginView.as_view(), name="Login"),
    path('profile/', UserProfileView.as_view(), name="Profile"),
    path('change-password/', UserChangePasswordView.as_view(),
         name="Change password")

]
