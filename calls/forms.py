from django.forms import ModelForm, TimeInput, TextInput, Textarea
from django.forms.widgets import CheckboxInput, Select, EmailInput, DateInput, RadioSelect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


################################################## User ############################################################

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


################################################## Call ############################################################

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
 

class AssignRespondersForm(ModelForm):
    class Meta:
        model = Call
        fields = ['responder']
        widgets = {
            'responder': Select(attrs={'type': 'text', 'class': 'no-arrow text-center'})
        }


################################################## Walkin ############################################################

class WalkinForm(ModelForm):
    class Meta:
        model = Walkin
        fields = ['firstname', 'lastname', 'department', 'reason',]
        widgets = {
            'firstname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'First Name', 'style': 'margin-bottom: 10px;'}),
            'lastname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Last Name', 'style': 'margin-bottom: 10px;'}),
            'department': Select(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'reason': TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Reason for visit...', 'style': 'margin-bottom: 10px;'}),
        }


class WalkinNotesForm(ModelForm):
    class Meta:
        model = Walkin
        fields = ['notes']
        widgets = {
            'notes': Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
        }


################################################## Responder ############################################################

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
        

################################################## Minor ############################################################

class MinorForm(ModelForm):
    class Meta:
        model = Minor
        fields = ['firstname', 'lastname', 'emp_id', 'dob', 'consent_scan']
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'emp_id': 'ID #',
            'dob': 'DOB',
            'consent_scan': 'Parental Consent Scan'
        }
        widgets = {
            'lastname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'firstname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'emp_id': TextInput(attrs={'type': 'text', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
            'dob': DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
        }


class UpdateMinorConsentForm(ModelForm):
    class Meta:
        model = Minor
        fields = ['consent_scan']


################################################## Schedule ############################################################

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        labels = {
            
        }
        widgets = {
            't_1': TimeInput(attrs={'type': 'time', 'style': 'margin-bottom: 10px;'}),
            't_2': TimeInput(attrs={'type': 'time', 'style': 'margin-bottom: 10px;'}),
            't_3': TimeInput(attrs={'type': 'time', 'style': 'margin-bottom: 10px;'}),
            't_4': TimeInput(attrs={'type': 'time', 'style': 'margin-bottom: 10px;'}),
            't_5': TimeInput(attrs={'type': 'time', 'style': 'margin-bottom: 10px;'}),
            't_6': TimeInput(attrs={'type': 'time', 'style': 'margin-bottom: 10px;'}),
            'p5_1': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p5_2': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p5_3': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p5_4': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p5_5': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p5_6': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p10_6': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p10_1': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p10_2': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p10_3': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p10_4': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p10_5': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p10_6': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p20_1': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p20_2': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p20_3': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p20_4': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p20_5': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p20_6': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p30_1': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p30_2': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p30_3': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p30_4': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p30_5': TextInput(attrs={'type': 'text', 'class': 'w-75'}),
            'p30_6': TextInput(attrs={'type': 'text', 'class': 'w-75'}) 
        }
