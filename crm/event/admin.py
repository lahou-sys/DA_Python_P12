from django.contrib import admin

from .models import Event

from base_admin.admin import base_admin_interface


class BaseEventAdmin(admin.ModelAdmin):

    list_display = [
        'contract',
        'support_contact',
        'sales_contact',
        'client',
        'attendees',
        'event_date',
        'completed',
        'date_created',
        'date_updated',
    ]

    search_fields = [
        'contract__project_name',
        'contract__client__last_name',
        'contract__client__first_name',
        'contract__client__email',
    ]

    list_filter = (
        'date_created',
        'event_date',
        'completed',
    )

    def client(self, obj):
        return obj.contract.client

    def sales_contact(self, obj):
        return obj.contract.client.sales_contact.username



base_admin_interface.register(Event,BaseEventAdmin)

