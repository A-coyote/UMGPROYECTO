from django import forms
from .models import categoria
from .models import producto

class categorias(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'



class productos(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'
