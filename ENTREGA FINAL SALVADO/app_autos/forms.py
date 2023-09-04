from django import forms
from .models import Coche

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = ['marca', 'modelo', 'año', 'descripcion', 'precio']
