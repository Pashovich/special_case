from django import forms
from .models import ModelData


class Form(forms.ModelForm):
    class Meta:
        model = ModelData
        fields = ['name', 'email']
