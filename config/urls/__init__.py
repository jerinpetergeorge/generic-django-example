from django.urls import include, path

urlpatterns = [
    path("", include("config.urls.default")),
    path("drf-yasg/", include("config.urls.drf_yasg", namespace="drf-yasg")),
    path(
        "drf-spectacular/",
        include("config.urls.drf_spectacular", namespace="drf-spectacular"),
    ),
    path("api/v1/", include("config.urls.apis")),
]
