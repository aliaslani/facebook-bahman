from email import message

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from core.models import User, Post
from core.forms import NewPostForm


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
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post':post
    }
    return render(request, 'core/post_detail.html', context=context)


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'پست شما با موفقیت حذف شد')
    return redirect('post_list')


# def new_post(request):
    # form = NewPostForm()
    # if request.method == 'POST':
    #     form = NewPostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         title = data.get('title')
    #         content = data.get('content')
    #         user = data.get('user')
    #         image = data.get('image')
    #         new_post = Post.objects.create(title=title, content=content, user=user,image=image)
    #         messages.success(request, 'پست شما با موفقیت ساخته شد')
    #         return redirect('post_list')
    # context = {
    #     'form':form
    # }
    # return render(request, 'core/new_post.html', context=context)


def new_post(request):
    form = NewPostForm()
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'پست شما با موفقیت ساخته شد')
            return redirect('post_list')
    
    return render(request, 'core/new_post.html', context={'form':form})

def edit_post(request, post_id):
    p = Post.objects.filter(pk=post_id)
    post = p.first()
    
    form = NewPostForm(initial={'title':post.title, 'content':post.content, 'user':post.user})
    if request.method == 'POST':
        form = NewPostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        # form = NewPostForm(request.POST, request.FILES)
        # if form.is_valid():
        #     title = form.cleaned_data.get('title')
        #     content = form.cleaned_data.get('content')
        #     user = form.cleaned_data.get('user')
        #     image = form.cleaned_data.get('image')
        #     p.update(title=title, content=content, user=user, image=image)
            messages.success(request, 'پست شما با موفقیت ویرایش شد')
            return redirect('post_detail', post_id=post.id)
    return render(request, 'core/edit_post.html', context={'form':form, 'p':post})
