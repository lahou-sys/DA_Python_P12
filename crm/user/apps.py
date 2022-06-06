from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .add_permissions_managers import create_permissions


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        post_migrate.connect(create_permissions, sender=self)