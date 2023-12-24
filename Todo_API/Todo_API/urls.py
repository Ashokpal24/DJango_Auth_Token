from django.contrib import admin
from django.urls import path, include
from Auth import urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(auth_urls))
]
