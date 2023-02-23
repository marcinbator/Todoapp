from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@login_required
def dashboard(request):
  return render(request, 'dashboard.html')


@csrf_exempt
def register(request):
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('users:dash')
    else:
      for field, errors in form.errors.items():
        for error in errors:
          messages.error(request, f" {error}")
    return redirect('users:register')
  context = {'form': form}
  return render(request, 'register.html', context)


@csrf_exempt
def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Zalogowano.')
      return redirect('users:dash')
    else:
      messages.error(request, 'Błąd logowania..')
      return redirect('login')
  else:
    return render(request, 'login.html')


@csrf_exempt
@login_required
def logout_view(request):
  logout(request)
  messages.success(request, 'Wylogowano.')
  return redirect('home')
