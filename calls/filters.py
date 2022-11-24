import django_filters
from django_filters import CharFilter

from .models import *


class ResponderFilter(django_filters.FilterSet):

    class Meta:
        model = Responder
        fields = ['lastname', 'status', 'certification']


class CallFilter(django_filters.FilterSet):

    location = CharFilter(field_name="location", lookup_expr="icontains")

    class Meta:
        model = Call
        fields = ['nature', 'responder', 'red']


class WalkinFilter(django_filters.FilterSet):

    reason = CharFilter(field_name="reason", lookup_expr="icontains")
    notes = CharFilter(field_name="notes", lookup_expr="icontains")
    
    class Meta:
        model = Walkin
        fields = '__all__'
        exclude = ['datetime', 'firstname', 'notes', 'reason']
