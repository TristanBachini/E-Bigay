from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields.files import FileField, ImageFieldFile
from .models import *
from django import forms
from django.forms import ModelForm,TextInput, PasswordInput, CharField, HiddenInput,NumberInput, widgets
from django.forms.widgets import Select
from django.forms.widgets import DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AyudaApplicantForm(ModelForm):
    class Meta:
        model = AyudaApplicant
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={'class':'form-control', 'min':'1'}),
            'city' : Select(attrs={'class':'form-control', 'min':'1'}),
            'dateofbirth': DateInput(attrs={'type': 'date'}),
            'street1' : TextInput(attrs={'class':'form-control', 'min':'1'}),
            'street2' : TextInput(attrs={'class':'form-control', 'min':'1'}),
            'region' : Select(attrs={'class':'form-control', 'min':'1'}),
            'user': HiddenInput(attrs = {'type':'hidden'} )
        }

class UserForm(UserCreationForm):
    attrs={'class':'form-control','id':'floatingInput','placeholder':'Enter Password', 'required':True}
    password1 = CharField(widget = PasswordInput(attrs=attrs))
    password2 = CharField(widget = PasswordInput(attrs=attrs))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'First name', 'aria-label':'First name','required':True}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder':'Last name', 'aria-label':'Last name','required':True}),
            'username': TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'aria-label':'Username','required':True}),
            'email':TextInput(attrs={'class':'form-control', 'placeholder':'Email', 'aria-label':'Email','required':True}),

        }

class CityForm(ModelForm):
    class Meta:
        model = CityChoice
        fields = "__all__"
        widgets = {
            'city':Select(attrs={'class':'form-control', 'min':'1'})
        }

class AyudaDropoffForm(ModelForm):
    class Meta:
        model = AyudaDropoff
        fields = "__all__"

