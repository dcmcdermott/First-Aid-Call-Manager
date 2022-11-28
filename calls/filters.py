import django_filters
from django_filters import CharFilter, DateFilter, BooleanFilter, ChoiceFilter, ModelChoiceFilter
from django.forms import DateTimeInput, CheckboxInput, TextInput, Select

from .models import *


class ResponderFilter(django_filters.FilterSet):

    CERTIFICATIONS = (
        ('EMT-B', 'EMT-B'),
        ('EMT-P', 'EMT-P'),
        ('LPN', 'LPN'),
        ('RN', 'RN')
    )
    STATUS = (
        ('PT', 'PT'),
        ('PT-S', 'PT-S'),
        ('FT-S', 'FT-S')
    ) 

    lastname = CharFilter(field_name="lastname", widget=TextInput(attrs={'class': 'form-control ml-2 mr-2'}))
    certification = ChoiceFilter(field_name="certification", choices=CERTIFICATIONS,  label= 'Certification', widget=Select(attrs={'class': 'form-control ml-2 mr-2'}))
    ft_pt = ChoiceFilter(field_name="status", choices=STATUS, label= 'FT/PT', widget=Select(attrs={'class': 'form-control ml-2 mr-2'}))

    class Meta:
        model = Responder
        fields = ['lastname', 'certification', 'ft_pt']


class CallFilter(django_filters.FilterSet):

    CALL_TYPES = (
        ('A', 'A - ALLERGIC REACTION'),
        ('B', 'B - BITE/STING'),
        ('C', 'C - CARDIAC'),
        ('E', 'E - EXPOSURE'),
        ('F', 'F - FAINT'),
        ('G', 'G - GUEST ASSISTANCE'),
        ('H', 'H - HEAT RELATED'),
        ('I', 'I - ILLNESS'),
        ('R', 'R - RESPIRATORY'),
        ('T', 'T - TRAUMA'),
        ('U', 'U - UNKNOWN'),
        ('X', 'X - SEIZURE')
    )
    ZONES = (
        ('701', '701'),
        ('705', '705'),
        ('710', '710'),
        ('720', '720'),
        ('730', '730'),
        ('740', '740'),
        ('745', '745'),
    )
    call_date = DateFilter(field_name="datetime__date", label= 'Date', widget=DateTimeInput(attrs={'type': 'date', 'class': 'form-control ml-2 mr-2'}))
    nature = ChoiceFilter(field_name="nature", choices=CALL_TYPES, widget=Select(attrs={'class': 'form-control ml-2 mr-2'}))
    zone = ChoiceFilter(field_name="zone", choices=ZONES, widget=Select(attrs={'class': 'form-control ml-2 mr-2'}))
    location = CharFilter(field_name="location", label= 'Location', lookup_expr="icontains", widget=TextInput(attrs={'class': 'form-control ml-2 mr-2'}))
    red = BooleanFilter(field_name="red", widget=CheckboxInput(attrs={'class': 'form-control ml-2 mr-2'}))
    responder = ModelChoiceFilter(queryset=Responder.objects.all(), field_name="responder", widget=Select(attrs={'class': 'form-control ml-2 mr-2'}))
    
    class Meta:
        model = Call
        fields = ['red', 'call_date','nature', 'zone', 'location', 'responder']


class WalkinFilter(django_filters.FilterSet):

    DEPARTMENTS = (
        ('Culinary', 'Culinary'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Games', 'Games'),
        ('Grounds', 'Grounds'),
        ('Guest Relations', 'Guest Relations'),
        ('HR', 'HR'),
        ('Maintenance', 'Maintenance'),
        ('Merchandise', 'Merchandise'),
        ('Security', 'Security'),
        ('Traffic', 'Traffic'),
        ('Zoo', 'Zoo'),
    )
    walkin_date = DateFilter(field_name="datetime__date", label= 'Date', widget=DateTimeInput(attrs={'type': 'date', 'class': 'form-control ml-2 mr-2'}))
    lastname = CharFilter(field_name="lastname", widget=TextInput(attrs={'class': 'form-control ml-2 mr-2'}))
    department = ChoiceFilter(field_name="department", choices=DEPARTMENTS, widget=Select(attrs={'class': 'form-control ml-2 mr-2'}))
    reason = CharFilter(field_name="reason", label= 'Reason', lookup_expr="icontains", widget=TextInput(attrs={'class': 'form-control ml-2 mr-2'}))
    
    
    class Meta:
        model = Walkin
        fields = ['walkin_date', 'lastname', 'department', 'reason']
