from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator, FileExtensionValidator, RegexValidator, DecimalValidator
from core.models import Post


# class NewPostForm(forms.Form):
#     title = forms.CharField(label='عنوان'  ,widget=forms.TextInput(attrs={'class':'form-control mt-1'}))
#     content = forms.CharField(validators=[MinLengthValidator(10, 'این فیلد نمی تواند کمتر از ۱۰ کاراکتر باشد'), MaxLengthValidator(20, 'باید کمتر از ۲۰ کاراکتر باشد' \
#     '')], widget=forms.Textarea(attrs={'class':'form-control'}))
#     user = forms.ModelChoiceField(queryset=User.objects.all(), label='کاربر', widget=forms.Select(attrs={'class':'form-select'}))
#     image = forms.ImageField(label='تصویر', required= False  ,validators=[FileExtensionValidator(['jpg','png','jpeg'], 'یک تصویر معتبر بارگذاری کنید. فایلی که بارگذاری کردید یا تصویر نبوده و یا تصویری مخدوش بوده است.')], widget=forms.FileInput(attrs={'class':'form-control'}))


#     def clean_title(self):
#         value = self.cleaned_data.get('title')
#         if len(value) < 3:
#             raise ValidationError('خیلی کوتاه است')
#         return value
    
#     def clean_content(self):
#         content = self.cleaned_data.get('content')
#         word_invalid_list = ['فحش', 'زشت']
#         for i in word_invalid_list:
#             if i in content:
#                 raise ValidationError(f'این حرفها نباید در محتوای پست وجود داشته باشد{i}')
#         return content
    
#     def clean(self):
#         data = super().clean()
#         title = data.get('title')
#         content = data.get('content')
#         if title and content and  not title in content:
#             raise ValidationError('عنوان حتما باید در محتوا باشد')
#         return data


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content', 'user','image']


        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control mt-2'})
        }

