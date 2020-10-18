from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.urls import reverse

from django.core.mail import send_mail

from MovieBlog.celery import app

from django.contrib.auth import get_user_model


def send_verification_mail_queryset_processing(user_id):
	try:
		UserModel = get_user_model()
		user = UserModel.objects.get(pk=user_id)
		
	except UserModel.ObjectDoesNotExist:
		logging.warning('Tried to send verification email to '\
			'non-existing <user_id:{}>'.format(user_id))

	finally:
		return (user.email, user.verification_uuid)


@app.task
def send_verification_mail(user_id):
	email, uuid = send_verification_mail_queryset_processing(user_id)
	
	VERIFICATION_URL = 'http://localhost:8000'
	VERIFICATION_VIEW =	reverse(
	    'AppAuth:verified_account', 
	    kwargs={'uuid': str(uuid)}
	)

	send_mail(
       	f'Hello, {email}! verify your account',
       	'Follow this link to verify your account: '\
       	    f'{VERIFICATION_URL}{VERIFICATION_VIEW}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
	)
