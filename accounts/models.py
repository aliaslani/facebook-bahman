from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='profile_picture/avatar.jpg')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
