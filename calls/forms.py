from django.forms import ModelForm, TimeInput, TextInput, Textarea
from django.forms.widgets import CheckboxInput, Select, EmailInput, DateInput, RadioSelect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class CallForm(ModelForm):
    class Meta:
        model = Call
        fields = [ 'zone', 'red', 'nature', 'location', 'caller', 'responder']
        labels = {
            'red': 'Red?',
            'nature': 'Nature',
            'zone': '',
            'location': 'Location',
            'caller': 'Caller',
            'responder': 'Responder',
        }
        widgets = {
            'zone': RadioSelect(attrs={'type': 'text', 'class': 'form-check form-check-inline w-100'}),
            'red': CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check mb-1 ml-3'}),           
            'nature': Select(attrs={'type': 'text', 'class': 'form-control w-75 ml-auto mr-auto mb-1'}),
            'location': TextInput(attrs={'type': 'text', 'class': 'form-control w-75 ml-auto mr-auto mb-1', 'placeholder': 'Location...'}),
            'caller': TextInput(attrs={'type': 'text', 'class': 'form-control w-75 ml-auto mr-auto mb-1'}),
            'responder': Select(attrs={'type': 'text', 'class': 'form-control w-75 ml-auto mr-auto mb-1'}),
        }

 
class WalkinForm(ModelForm):
    class Meta:
        model = Walkin
        fields = ['firstname', 'lastname', 'department', 'reason',]
        widgets = {
            'firstname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'lastname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'department': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'reason': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
        }


class WalkinNotesForm(ModelForm):
    class Meta:
        model = Walkin
        fields = ['notes']
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
        }


class ResponderForm(ModelForm):
    class Meta:
        model = Responder
        fields = ['firstname', 'lastname', 'certification', 'status', 'phone', 'email', 'license_scan', 'license_expiration', 'cpr_scan', 'cpr_expiration', 'active']
        widgets = {
            'firstname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'lastname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'certification': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'status': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'phone': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'email': EmailInput(attrs={'type': 'email', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'cpr_expiration': DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'license_expiration': DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'active': CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check', 'style': 'margin-bottom: 10px;'}),
        }
       

class UpgradeForm(ModelForm):
    class Meta:
        model = Call
        fields = ['upgrade_time', 'ems_on_scene_time', 'ems_clear_scene_time'] 
        widgets = {
            'upgrade_time': TimeInput(attrs={'type': 'time', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'ems_on_scene_time': TimeInput(attrs={'type': 'time', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'ems_clear_scene_time': TimeInput(attrs={'type': 'time', 'class': 'form-control', 'style': 'margin-bottom: 10px;'})
        }

        
class DowngradeForm(ModelForm):
    class Meta:
        model = Call
        fields = ['nature'] 
        widgets = {
            'nature': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'})
        }
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class AssignRespondersForm(ModelForm):
    class Meta:
        model = Call
        fields = ['responder']
        widgets = {
            'responder': Select(attrs={'type': 'text', 'class': 'no-arrow text-center'})
        }