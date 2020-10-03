from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model 


class EmailOnlyBackend(BaseBackend):

	def authenticate(self, email, password):
		try:
			user = get_user_model().objects.get(email=email)
			if user.check_password(password):
				return user
		except get_user_model().DoesNotExist:
			return None
		else:
			return None

	def get_user(self, user_id):
		try:
			return get_user_model().objects.get(pk=user_id)
		except get_user_model().DoesNotExist:
			return None
