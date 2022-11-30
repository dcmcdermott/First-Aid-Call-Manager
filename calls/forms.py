from django.forms import ModelForm, TimeInput, TextInput, Textarea
from django.forms.widgets import CheckboxInput, Select, EmailInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class CallForm(ModelForm):
    class Meta:
        model = Call
        fields = ['red', 'nature', 'zone', 'location', 'caller', 'responder']
        widgets = {
            'red': CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check', 'style': 'margin-bottom: 10px;'}),
            'nature': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'zone': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'location': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'caller': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'responder': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
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
        fields = ['firstname', 'lastname', 'certification', 'status', 'phone', 'email', 'active']
        widgets = {
            'firstname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'lastname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'certification': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'status': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'phone': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'email': EmailInput(attrs={'type': 'email', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
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