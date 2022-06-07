from rest_framework import permissions


class EventPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user.groups.filter(name='sales').exists():
                return True
            elif request.user.groups.filter(name='support').exists():
                return True

        if request.method in ["PUT", "PATCH", "DELETE"]:
            if request.user.groups.filter(name='sales').exists():
                return True
            elif request.user.groups.filter(name='support').exists():
                return True

    def has_object_permission(self, request, view, obj):
        if (
            request.user == obj.support_contact and
            request.user.groups.filter(name='support').exists()
        ):
            return True
        elif (
            request.user == obj.contract.client.sales_contact and
            request.user.groups.filter(name='sales').exists()
        ):
            return True