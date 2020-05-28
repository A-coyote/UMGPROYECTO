from django import forms
from .models import venta_det

class ventas(forms.ModelForm):
    class Meta:
        model = venta_det
        fields = '__all__'
