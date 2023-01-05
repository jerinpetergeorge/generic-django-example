from django.shortcuts import render


def _demo_view(request, *args, **kwargs):
    return render(request, "general/drf-yasg.html")
