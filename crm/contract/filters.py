from django_filters import rest_framework as filters
from .models import Contract


class ContractFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name="amount", lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name="amount", lookup_expr='lte')

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (amount, -amount, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'signed',
            'min_amount',
            'max_amount',
            'client__id',
            'client__sales_contact',
            ]