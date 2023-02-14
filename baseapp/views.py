from django.shortcuts import render, redirect
from .models import Element
from .forms import addElement
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    context = {
        'elements': Element.objects.all()
    }
    return render(request, 'home.html', context)


def dodaj(request):
    form = addElement()
    if request.method == 'POST':
        form = addElement(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request, 'addElement.html', context)


def usun(request, id):
    Element.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('home'))
