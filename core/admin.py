from django.contrib import admin

from core.models import Post, User

admin.site.register(User)
admin.site.register(Post)
