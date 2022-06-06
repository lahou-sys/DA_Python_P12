from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.exceptions import ValidationError

from .models import Event
from contract.models import Contract
from contract.serializers_common import ContractNestedSerializer, ClientNestedSerializer


class EventListSerializer(serializers.ModelSerializer):

    contract = ContractNestedSerializer()
    support_contact = StringRelatedField()

    class Meta:
        model = Event
        fields = [
            'support_contact',
            'attendees',
            'event_date',
            'completed',
            'contract',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:event-detail"}
        }


class EventSerializer(serializers.ModelSerializer):

    contract = ContractNestedSerializer(read_only=True)
    support_contact = StringRelatedField()

    class Meta:
        model = Event
        fields = [
            'support_contact',
            'attendees',
            'event_date',
            'notes',
            'completed',
            'contract',
            'date_created',
            'date_updated',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:event-detail"}
        }
        read_only_fields = [
            'support_contact',
            'date_created',
            'date_updated',
        ]

    def validate_contract(self, contract_pk):
        contract = Contract.objects.get(pk=contract_pk)
        if Event.objects.filter(contract=contract).exists():
            raise ValidationError('An event already exists for this contract', code='unique')