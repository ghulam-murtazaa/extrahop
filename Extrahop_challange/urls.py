from django.contrib import admin
from django.urls import path
from .views import BaseAPIView, UserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseAPIView.as_view(), name="base-api-view"),
    path('user/<str:user_id>', UserAPIView.as_view(), name="user-api-view"),
]
