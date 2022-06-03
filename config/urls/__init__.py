from django.urls import include, path

urlpatterns = [
    path("", include("config.urls.default")),
    path("api/v1/", include("config.urls.apis")),
]
