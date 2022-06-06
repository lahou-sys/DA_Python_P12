from django_filters import rest_framework as filters
from models import Client


class ClientFilter(filters.FilterSet):

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (compane_name, -company_name, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'email',
            'converted'
        ]