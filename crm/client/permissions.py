from rest_framework import permissions


class ClientPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='sales').exists()

    def has_object_permission(self, request, view, obj):

        return request.user == obj.sales_contact