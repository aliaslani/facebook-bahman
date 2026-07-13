from django.urls import path
from core.views import say_hello, home, post_list, post_detail

urlpatterns = [
    path('hello/', say_hello, name='say_hello'),
    path('home/<username>/', home, name='home'),
    path('post/', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail')
]
