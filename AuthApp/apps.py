from django.apps import AppConfig

from django.db.models.signals import post_save
from .signals import user_creation_receiver

from django.contrib.auth import get_user_model


class AuthappConfig(AppConfig):
    name = 'AuthApp'

    def ready(self):
    	post_save.connect(user_creation_receiver, 
    		sender=get_user_model())
