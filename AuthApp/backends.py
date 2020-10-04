from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model 


class EmailOnlyBackend(BaseBackend):

	def __init__(self):
		self.CustomUserModel = get_user_model()

	def authenticate(self, request, email, password):
		try:
			user = self.CustomUserModel.objects.get(email=email)
			if user.check_password(password):
				return user
		except self.CustomUserModel.DoesNotExist:
			return None
		else:
			return None

	def get_user(self, user_id):
		try:
			return self.CustomUserModel.objects.get(pk=user_id)
		except self.CustomUserModel.DoesNotExist:
			return None
