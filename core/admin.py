from django.contrib import admin

# Register your models here.

from core.models import Post, User

admin.site.register(User)
admin.site.register(Post)