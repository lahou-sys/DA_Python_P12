from django.contrib import admin
from .models import Contract

from base_admin.admin import base_admin_interface

class BaseContractAdmin(admin.ModelAdmin):
    
    list_display = [
        'project_name',
        'id',
        'client',
        'signed',
        'amount',
        'payment_due_date',
        'date_created',
        'date_updated',
    ]
    
    search_fields = [
        'project_name',
        'client__first_name',
        'client__last_name',
        'client__email',
        'date_created',
        'amount',
    ]
    
    list_filter = (
        'date_created',
        'payment_due_date',
        'date_updated',
        'signed'
    )

base_admin_interface.register(Contract, BaseContractAdmin)