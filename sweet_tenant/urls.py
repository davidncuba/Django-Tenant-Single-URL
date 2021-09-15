from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SweetViewSet

urlpatterns = [
    path("", SweetViewSet.as_view()),
]
