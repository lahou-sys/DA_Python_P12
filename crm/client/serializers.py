from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Client
from contract.serializers_common import ContractNestedSerializer


class ClientListSerializer(serializers.ModelSerializer):

    sales_contact = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'email',
            'converted',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:client-detail"}
        }


class ClientSerializer(serializers.ModelSerializer):

    contracts = ContractNestedSerializer(many=True, read_only=True)
    sales_contact = StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'email',
            'phone',
            'mobile',
            'converted',
            'contracts',
            'date_created',
            'date_updated',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:client-detail"}
        }
        read_only_fields = [
            'converted',
            'sales_contact',
            'date_created',
            'date_updated',
        ]