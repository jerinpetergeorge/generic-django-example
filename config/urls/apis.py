from django.urls import include, path

urlpatterns = [
    path("simple-jwt/", include("config.urls.drf_simple_jwt")),
    path("polls/", include(("polls.apis.urls", "polls"), namespace="polls-api")),
    path(
        "accounts/",
        include(("accounts.apis.urls", "accounts"), namespace="accounts-api"),
    ),
]
