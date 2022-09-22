from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Period


# Create your views here.
class MarkAttendanceView(LoginRequiredMixin, generic.TemplateView):
    template_name = "attendance/mark-attendance.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["disabled"] = ""
        if Period.is_marked_already(self.request.user):
            ctx["disabled"] = "disabled"

        return ctx

    def check_in(self):
        period = Period.get_current_period(self.request.user)
        period.mark_attendance()

    def post(self, request, *args, **kwargs):
        self.check_in()
        return self.get(request, *args, **kwargs)
