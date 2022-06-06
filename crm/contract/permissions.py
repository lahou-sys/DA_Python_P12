from rest_framework import permissions


class ContractPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user == obj.client.sales_contact