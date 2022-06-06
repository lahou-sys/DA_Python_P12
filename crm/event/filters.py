from django_filters import rest_framework as filters
from .models import Event


class EventFilter(filters.FilterSet):

    min_attendees = filters.NumberFilter(field_name="attendees", lookup_expr='gte')
    max_attendees = filters.NumberFilter(field_name="attendees", lookup_expr='lte')

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (event_date, -event_date, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Event
        fields = [
            'support_contact',
            'attendees',
            'event_date',
            'completed',
            'contract__id',
            'contract__project_name',
        ]