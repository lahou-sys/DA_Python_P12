from rest_framework import permissions
from event.models import Event
from contract.models import Contract


class ClientPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user.groups.filter(name='sales').exists():
                return True
            elif request.user.groups.filter(name='support').exists():
                return True

    def has_object_permission(self, request, view, obj):
        client_id = str(request).split('/')
        current_user = request.user
        id_user = current_user.id
        client_to_view = int(client_id[-2])

        list_event_of_user = []
        for event in Event.objects.filter(support_contact__id=id_user).values_list('contract_id'):
            list_event_of_user.append(event[0])

        list_client_of_user = []
        for event in list_event_of_user:
            client = Contract.objects.filter(id=event).values_list('client_id')
            list_client_of_user.append(client[0][0])

        if client_to_view in list_client_of_user:
            return True
        
        return request.user == obj.sales_contact
