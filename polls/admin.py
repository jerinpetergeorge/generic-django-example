from django.apps import apps
from django.contrib import admin

from .models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ("votes",)
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ["question"],
            },
        ),
    ]
    inlines = [ChoiceInline]
    list_display = ("question",)
    search_fields = ["question"]


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)

# auto register apps
app_name = "polls"
app = apps.get_app_config(app_name)

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
