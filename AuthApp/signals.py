from django.db.models import signals

from .tasks import send_verification_mail  # import Celery task


def user_creation_receiver(sender, instance, **kwargs):
	if not instance.is_verified:
		send_verification_mail.delay(instance.pk)  # Run celery task
