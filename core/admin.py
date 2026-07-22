from django.contrib import admin
from core.models import Post, CustomUser

admin.site.register(CustomUser)
admin.site.register(Post)
