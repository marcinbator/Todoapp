from django.shortcuts import render, redirect
from .models import Element
from .forms import addElement
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        elements = Element.objects.filter(author=request.user)
    else:
        elements = []
    context = {
        'elements': elements
    }
    return render(request, 'home.html', context)


@login_required
def dodaj(request):
    form = addElement()
    if request.method == 'POST':
        form = addElement(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request, 'addElement.html', context)


@login_required
def usun(request, id):
    Element.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('home'))


@login_required
def edytuj(request, id):
    element = Element.objects.get(id=id)
    if request.method == 'POST':
        form = addElement(request.POST, instance=element)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addElement(instance=element)
    context = {
        'form': form
    }
    return render(request, 'addElement.html', context)


@login_required
def switchDone(request, id):
    element = Element.objects.get(id=id)
    element.done = not element.done
    element.save()
    elements = Element.objects.all()
    context = {
        'elements': elements
    }
    return render(request, 'home.html', context)
