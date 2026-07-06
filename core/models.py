from tabnanny import verbose

from django.db import models


class CountryChoices(models.TextChoices):
    IRAN = ('iran','ایران')
    FRANCE=('france', 'فرانسه')


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='نام کاربری')
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    email = models.EmailField()
    coutry = models.CharField(max_length=20, choices=CountryChoices.choices, default=CountryChoices.IRAN)
    phone = models.CharField(max_length=11)
    height = models.PositiveSmallIntegerField(null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.username}:{self.email}'
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_upate = models.DateTimeField(auto_now=True)


