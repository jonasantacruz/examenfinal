from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('isbn','author','title', 'editorial','pais','anio',)
