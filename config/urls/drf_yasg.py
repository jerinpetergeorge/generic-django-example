from django.conf import settings
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from ..views import _demo_view

app_name = "drf_yasg"


urlpatterns = [
    path("any/", _demo_view, name="schema-swagger-ui"),
]

if settings.DRF_YASG_AVAILABLE:
    schema_view = get_schema_view(
        openapi.Info(
            title="Generic Django APIs",
            default_version="v1",
            description="Simple APIs to use Generic Django Project",
            contact=openapi.Contact(email="jerinpetergeorge@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/$",
            schema_view.with_ui(
                "redoc",
                cache_timeout=0,
            ),
            name="schema-redoc",
        ),
    ]
