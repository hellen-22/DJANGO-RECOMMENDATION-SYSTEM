from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from .models import*


class CustomUserForm(UserCreationForm):
    registration_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs=
        {'class': 'form-control',
         'placeholder':'Registration Number',
         'id':'registration_number'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs=
        {'class': 'form-control',
         'placeholder': 'Student Email',
         'id':'email'}))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs=
        {'placeholder': 'Password'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs=
        {'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ('registration_number', 'email', 'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['confirm_password'].widget.attrs['class'] = 'form-control'



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')


class AccountEditForm(UserChangeForm):
    registration_number = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('registration_number', 'email')
