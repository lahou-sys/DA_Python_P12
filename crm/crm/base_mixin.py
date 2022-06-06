from rest_framework import  mixins
from rest_framework.response import Response

class CustomListMixin:
    """
    Custom List View that allows to specify a different serializer for displaying
    a list of objects. This class shall be inherited in conjuction with a viewset class.
    The parameter list_serializer_class shall be set to the serializer used for list
    display.
    """

    def list(self, request, filter=None, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if filter is not None:
            queryset = queryset.filter(**filter)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_list_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_list_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_list_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for the list view.
        """
        serializer_class = self.list_serializer_class
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)