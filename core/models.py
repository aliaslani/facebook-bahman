from tabnanny import verbose

from django.db import models


class CountryChoices(models.TextChoices):
    IRAN = ('iran', 'ایران')
    FRANCE = ('france', 'فرانسه')


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='نام کاربری')
    password = models.CharField(max_length=20, verbose_name='رمز عبور')
    name = models.CharField(max_length=50, verbose_name='نام')
    birthdate = models.DateField(null=True, verbose_name='تاریخ تولد')
    email = models.EmailField(verbose_name='آدرس ایمیل')
    coutry = models.CharField(
        max_length=20, choices=CountryChoices.choices, default=CountryChoices.IRAN, verbose_name='کشور')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    height = models.PositiveSmallIntegerField(null=True, verbose_name='قد')
    income = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='درآمد')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='موضوع')
    content = models.TextField(verbose_name='محتوا')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='ساخته شده توسط:')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='ساخته شده در:')
    last_upate = models.DateTimeField(
        auto_now=True, verbose_name='آخرین تغییرات')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
