from django.contrib import admin
from .models import Client

from base_admin.admin import base_admin_interface


class BaseClientAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'mobile',
        'company_name',
        'converted',
        'date_created',
        'date_updated',
    ]

    search_fields = [
        'first_name',
        'last_name',
        'email',
        'company_name',
    ]

    list_filter = (
        'company_name',
        'converted',
        'date_created',
    )


base_admin_interface.register(Client, BaseClientAdmin)
