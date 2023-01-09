from django.urls import path

from .views import UserDetailAPI

urlpatterns = [
    path("who-am-i/", UserDetailAPI.as_view(), name="who-am-i"),
]
