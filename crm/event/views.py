import logging

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .permissions import EventPermission
from .filters import EventFilter
from event.serializers import EventSerializer, EventListSerializer
from crm.base_mixin import CustomListMixin, mixins


logger = logging.getLogger(__name__)


class EventViewSet(CustomListMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated, EventPermission]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    list_serializer_class = EventListSerializer
    filterset_class = EventFilter
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        'contract__client__first_name',
        'contract__client__last_name',
        'contract__client__email',
        'event_date',
        ]
    filterset_fields = [
        'support_contact',
        'attendees',
        'event_date',
        'completed',
        'contract__project_name',
        'min_attendees',
        'max_attendees',
        ]

    @action(methods=['GET'], detail=False)
    def me(self, request):
        logger.error(f'{request.user}')
        logger.error('Something went wrong!')
        return self.list(request=request, filter={'support_contact': request.user})
    
