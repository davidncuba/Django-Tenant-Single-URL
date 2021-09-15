from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
    path("api/login/", LoginAPI.as_view(), name="login"),
    path("api/logout/", knox_views.LogoutView.as_view(), name="logout"),
    path("api/logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
]
