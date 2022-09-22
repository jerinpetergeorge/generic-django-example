from django.conf import settings
from django.db import models
from django.utils import timezone


class Manager(models.Manager):
    def active(self, *args, **kwargs):
        return self.get_queryset().filter(
            start__lte=timezone.now().date(),
            end__gte=timezone.now().date(),
            *args,
            **kwargs,
        )


class Period(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()

    objects = Manager()

    def __str__(self):
        return f"{self.name} ({self.start} - {self.end})"

    @property
    def is_active(self):
        return self.start <= timezone.now().date() <= self.end

    @classmethod
    def is_marked_already(cls, user):
        try:
            period = cls.objects.active(user=user).get()
        except Period.DoesNotExist:
            return False
        return period.attendance_set.filter(date=timezone.now().date()).exists()

    @classmethod
    def get_current_period(cls, user):
        return cls.objects.active(user=user).get()

    def mark_attendance(self):
        attendance = Attendance.objects.create(
            period=self,
            date=timezone.now().date(),
            present=True,
        )
        return attendance


class Attendance(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["period", "date"],
                name="unique_attendance",
            ),
        ]

    def __str__(self):
        return f"{self.period.name} {self.date} {self.present}"
