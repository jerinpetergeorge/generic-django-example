from django.urls import path

from .schema import schema
from .views import GraphQLView

urlpatterns = [
    path("", GraphQLView.as_view(schema=schema)),
]
