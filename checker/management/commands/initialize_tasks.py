from django.core.management.base import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    help = "Initialize periodic tasks"

    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=5,
            period=IntervalSchedule.MINUTES,
        )

        # Create a periodic task
        PeriodicTask.objects.create(
            interval=schedule,
            name="Check website changes",
            task="checker.tasks.notify_about_changes",  # The task to run
        )

        self.stdout.write(self.style.SUCCESS("Successfully initialized periodic tasks"))
