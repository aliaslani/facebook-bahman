from django.db import models

# Create your models here.
class CountryChoices(models.TextChoices):
    IRAN = ('iran','ایران')
    FRANCE = ('france','فرانسه')




class User(models.Model):
    username = models.CharField(max_length=50,verbose_name='نام کاربری')
    password = models.CharField(max_length=20,verbose_name='رمز عبور')
    name = models.CharField(max_length=50,verbose_name= 'نام')
    birthdate = models.DateField(null=True,verbose_name='تاریخ تولد')
    email = models.EmailField(verbose_name='ایمیل')
    country = models.CharField(max_length=20,choices=CountryChoices.choices, default=CountryChoices.IRAN,verbose_name='نام کشور')
    phone = models.CharField(max_length=11,verbose_name='تلفن')
    height = models.PositiveSmallIntegerField(default=True<verbose_name='قد')
    incom = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='درآمد')
    
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class Post(models.Model):
    title = models.CharField(max_length=225,verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(User , on_delete=models.CASCADE,verbose_name='نام کاربر')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    last_update = models.DateTimeField(auto_now=True,verbose_name='آخرین به روز رسانی')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'


    