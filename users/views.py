from django.shortcuts import render
from .forms import CreateUserForm


def dashboard(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
    context = {'form': form}
    return render(request, 'dashboard.html', context)
