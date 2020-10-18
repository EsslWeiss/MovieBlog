from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
import uuid

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin): 
	
	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'email'

	objects = CustomUserManager()
	
	email = models.EmailField('email address', unique=True)

	is_verified = models.BooleanField('verified', default=False)
	verification_uuid = models.UUIDField('Verification uuid key', 
		default=uuid.uuid4)

	is_staff = models.BooleanField('staff', default=False)
	is_active = models.BooleanField('active', default=True)
	date_joined = models.DateTimeField('Date joined', 
		default=timezone.now)
	
	class Meta:
		swappable = 'AUTH_USER_MODEL'
		