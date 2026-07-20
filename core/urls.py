from django.urls import path
from core.views import say_hello, home, post_list, post_detail, post_delete, new_post, edit_post

urlpatterns = [
    path('hello/', say_hello, name='say_hello'),
    path('home/<username>/', home, name='home'),
    path('post/', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/delete/<int:post_id>/', post_delete, name='post_delete'),
    path('post/new/', new_post, name='new_post'),
    path('post/edit/<int:post_id>/', edit_post, name='edit_post'),
]
