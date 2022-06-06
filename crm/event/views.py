import logging

from rest_framework import viewsets
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

    @action(methods=['GET'], detail=False)
    def me(self, request):
        return self.list(request=request, filter={'support_contact': request.user})
