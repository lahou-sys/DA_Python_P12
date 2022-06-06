from rest_framework import permissions


class EventPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user == obj.support_contact