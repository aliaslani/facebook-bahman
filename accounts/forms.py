from django.core.exceptions import ValidationError
from django import forms
from accounts.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=50, label='گذرواژه', widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))



class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=60, label='تکرار گذرواژه', widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name', 'email','password', 'confirm_password', 'phone_number', 'profile_picture']



    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if not password == confirm_password:
            raise ValidationError('گذرواژه با تکرار آن مطابقت نداشت')
        return data