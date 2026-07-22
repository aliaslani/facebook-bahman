from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from accounts.forms import LoginForm, RegisterForm
from accounts.models import CustomUser

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'خوش آمدید')
                return redirect('post_list')
    return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
    logout(request)
    messages.success(request, 'شما با موفقیت خارج شدید')
    return redirect('login')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            messages.success(request, 'شما با موفقیت ثبت نام کردید')
            return redirect('login')
    return render(request, 'accounts/register.html',context={'form':form})