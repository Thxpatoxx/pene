from django import forms
from .models import Implementodep

class ImplementodepForm(forms.ModelForm):

    class Meta:
        model = Implementodep
        fields = ('implemento','estado','observación',)

class ImplementodepeditForm(forms.ModelForm):

    class Meta:
        model = Implementodep
        fields = ('estado','observación',)