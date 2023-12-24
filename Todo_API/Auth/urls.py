from django.urls import path
from Auth.views import UserRegisterationView

urlpatterns = [
    path('register/', UserRegisterationView.as_view(), name="Registeration")
]
