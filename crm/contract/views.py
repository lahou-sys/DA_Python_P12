import logging

from rest_framework import status, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Contract
from .permissions import ContractPermission
from .filters import ContractFilter
from event.models import Event
from event.serializers import EventSerializer, EventListSerializer
from contract.serializers import ContractSerializer, ContractListSerializer
from crm.base_mixin import CustomListMixin, mixins


logger = logging.getLogger(__name__)


class ContractViewSet(CustomListMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated, ContractPermission]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    list_serializer_class = ContractListSerializer
    filterset_class = ContractFilter
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        'id',
        'client__first_name',
        'client__last_name',
        'client__email',
        'date_created',
        'amount',
        ]
    filterset_fields = [
        'id',
        'project_name',
        'signed',
        'min_amount',
        'max_amount',
        'client__id',
        'client__sales_contact',
        ]


    @action(methods=['GET', 'POST'], detail=True)
    def events(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        if request.method == 'POST':
            serializer = EventSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.validate_contract(pk)
            serializer.save(contract=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            queryset = Event.objects.filter(contract=pk)
            page = self.paginate_queryset(queryset)
            serializer = EventListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

    @action(methods=['GET'], detail=False)
    def me(self, request):
        return self.list(request=request, filter={'client__sales_contact': request.user})
