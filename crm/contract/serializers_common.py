from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Contract
from client.models import Client


class ContractNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'url',
            'client_id',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:contract-detail"}
        }




class ClientNestedSerializer(serializers.ModelSerializer):

    sales_contact = StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:client-detail"}
        }
