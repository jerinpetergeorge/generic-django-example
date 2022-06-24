from django.urls import include, path

urlpatterns = [
    path("", include("config.urls.default")),
    path("drf-yasg/", include("config.urls.drf_yasg")),
    path("api/v1/", include("config.urls.apis")),
]
