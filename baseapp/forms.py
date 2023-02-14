from .models import Element
from django.forms import ModelForm


class addElement(ModelForm):
    class Meta:
        model = Element
        fields = ['title', 'content']
