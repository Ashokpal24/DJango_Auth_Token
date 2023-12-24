from django.urls import path
from Auth.views import (
    UserRegisterationView,
    UserLoginView
)

urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name="Registeration"),
    path('login/', UserLoginView.as_view(), name="Login")
]
