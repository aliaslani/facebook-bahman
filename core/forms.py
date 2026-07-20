from django import forms
from django.core.exceptions import ValidationError
from core.models import User

class NewPostForm(forms.Form):
    title = forms.CharField(label='عنوان', widget=forms.TextInput(attrs={'class':'form-control mt-1'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='کاربر', widget=forms.Select(attrs={'class':'form-select'}))
    image = forms.ImageField()

