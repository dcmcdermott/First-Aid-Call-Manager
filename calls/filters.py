import django_filters
from django_filters import CharFilter, DateFilter, BooleanFilter, ChoiceFilter
from django.forms import DateTimeInput, CheckboxInput

from .models import *


class ResponderFilter(django_filters.FilterSet):

    STATUS = (
        ('PT', 'PT'),
        ('PT-S', 'PT-S'),
        ('FT-S', 'FT-S')
    ) 

    ft_pt = ChoiceFilter(field_name="status", choices=STATUS, label= 'FT/PT')

    class Meta:
        model = Responder
        fields = ['lastname', 'certification', 'ft_pt']


class CallFilter(django_filters.FilterSet):

    location = CharFilter(field_name="location", lookup_expr="icontains")
    call_date = DateFilter(field_name="datetime__date", label= 'Date', widget=DateTimeInput(attrs={'type': 'date'}))
    red = BooleanFilter(field_name="red", label= 'Red', widget=CheckboxInput())

    class Meta:
        model = Call
        fields = ['call_date','nature', 'responder', 'red']


class WalkinFilter(django_filters.FilterSet):

    reason = CharFilter(field_name="reason", label= 'Reason', lookup_expr="icontains")
    walkin_date = DateFilter(field_name="datetime__date", label= 'Date', widget=DateTimeInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Walkin
        fields = ['walkin_date', 'lastname', 'department', 'reason']
