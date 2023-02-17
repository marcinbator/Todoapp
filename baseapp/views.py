from django.shortcuts import render, redirect
from .models import Element
from .forms import addElement
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def home(request):
    context = {
        'elements': Element.objects.filter(author=request.user)
    }
    return render(request, 'home.html', context)


def dodaj(request):
    form = addElement()
    if request.method == 'POST':
        form = addElement(request.POST)
        if form.is_valid:
            element = form.save(commit=False)
            element.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request, 'addElement.html', context)


def usun(request, id):
    Element.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('home'))
