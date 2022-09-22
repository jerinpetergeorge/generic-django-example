from django.contrib import admin

from .models import Attendance, Period


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "start", "end", "is_active")
    list_display_links = ("id", "name")


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "period", "date", "present")
    list_display_links = ("id", "period")
