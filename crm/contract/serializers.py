from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from .models import Contract
from .serializers_common import ClientNestedSerializer


class ContractListSerializer(serializers.ModelSerializer):

    client = ClientNestedSerializer()

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'signed',
            'amount',
            'client',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:contract-detail"}
        }


class ContractSerializer(serializers.ModelSerializer):

    client = ClientNestedSerializer(read_only=True)
    event = HyperlinkedRelatedField(view_name='api:event-detail', read_only=True)

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'signed',
            'amount',
            'payment_due_date',
            'client',
            'event',
            'date_created',
            'date_updated',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:contract-detail"}
        }
        read_only_fields = [
            'date_created',
            'date_updated',
            'event',
        ]
