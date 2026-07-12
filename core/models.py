from django.db import models


class CountryChoices(models.TextChoices):
    IRAN = ('iran','ایران')
    FRANCE=('france', 'فرانسه')


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='نام کاربری')
    password = models.CharField(max_length=20,verbose_name='گذرواژه')
    name = models.CharField(max_length=50,verbose_name='نام')
    birthdate = models.DateField(null=True,verbose_name='تاریخ تولد')
    email = models.EmailField(verbose_name='ایمیل')
    coutry = models.CharField(max_length=20, choices=CountryChoices.choices, default=CountryChoices.IRAN,verbose_name='کشور')
    phone = models.CharField(max_length=11,verbose_name='تلفن')
    height = models.PositiveSmallIntegerField(null=True,verbose_name='قد')
    income = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='درآمد')

    def __str__(self):
        return f'{self.username}:{self.email}'
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class Post(models.Model):
    title = models.CharField(max_length=255,verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نام')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')
    last_upate = models.DateTimeField(auto_now=True,verbose_name='آخرین ویرایش')


    def __str__(self):
        return self.title
    
    
    class Meta:
            verbose_name = 'پست'
            verbose_name_plural = 'پستها'
