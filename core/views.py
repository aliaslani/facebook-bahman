from django.shortcuts import render
from django.http import HttpResponse
from core.models import User, Post


def say_hello(request): #view function
    return HttpResponse('<h1 style="color: red; text-align:center;">Hello world!</h1>')

def home(request, username):
    name = User.objects.filter(username=username).first()
    context = {
        'first_name': name.name.capitalize() if name else 'World'
    }
    return render(request, 'core/index.html', context=context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'core/post_list.html', context=context)


def post_detail(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    context = {
        'post':post
    }
    return render(request, 'core/post_detail.html', context=context)