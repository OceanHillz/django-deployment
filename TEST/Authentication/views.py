from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm

def index(request):
    return render(request, 'Authentication/index.html', {})

def user_logout(request):
    logout(request)
    return redirect('authenticate:login')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f'Welcome {username}'))
            return redirect('authenticate:home')
        else:
            return redirect('authenticate:login')
    else:
        return render(request, 'Authentication/login.html', {})

def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, (f'Welcome {username}'))
            return redirect('authenticate:home')
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'Authentication/register.html', context)
