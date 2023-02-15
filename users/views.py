from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dash')
        else:
            messages.error(request, 'Chyba nie bardzo.')
            return redirect('register')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Wylogowano.')
    return redirect('home')
