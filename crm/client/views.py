import logging

from rest_framework import status, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Client
from contract.models import Contract
from .serializers import ClientSerializer, ClientListSerializer
from contract.serializers import ContractSerializer, ContractListSerializer
from .permissions import ClientPermission
from crm.base_mixin import CustomListMixin


logger = logging.getLogger(__name__)


class ClientViewSet(CustomListMixin, viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, ClientPermission]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    list_serializer_class = ClientListSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'id',
        'first_name',
        'last_name',
        'company_name',
        'sales_contact',
        'email',
        'converted'
        ]
    search_fields = [
        'id',
        'first_name',
        'last_name',
        'email',
        ]
    filterset_fields = [
        'id',
        'first_name',
        'last_name',
        'company_name',
        'sales_contact',
        'email',
        'converted'
        ]

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    @action(methods=['POST', 'GET'], detail=True)
    def contracts(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        if request.method == 'POST':
            client = self.get_object()
            serializer = ContractSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save(client=client)
            if not client.converted:
                client.converted = True
                client.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            queryset = Contract.objects.filter(client__pk=pk)
            page = self.paginate_queryset(queryset)
            serializer = ContractListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

    @action(methods=['GET'], detail=False)
    def me(self, request):
        logger.error(f'{request.user}')
        logger.error('Something went wrong!')
        return self.list(request=request, filter={'sales_contact': request.user})
    
    @action(methods=['GET'], detail=False)
    def prospects(self, request):
        return self.list(request=request, filter={'converted': False})
