from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from home.models import *

# Create your models here.

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['type'] = 'text'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['required'] = 'required'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['type'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['email'].widget.attrs['required'] = 'required'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['required'] = 'required'

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
        'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': (''),
        }

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'

        self.fields['receive_text'].widget.attrs['placeholder'] = 'Receive Texts?'

        self.fields['receive_email'].widget.attrs['placeholder'] = 'Receive Email?'

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'receive_text', 'receive_email')
