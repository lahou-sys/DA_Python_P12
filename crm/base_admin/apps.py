from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class BaseAdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_admin'


class BaseAdminSiteConfig(AdminConfig):
    default_site = 'base_admin.admin.BaseAdminSite'