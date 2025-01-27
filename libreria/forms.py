from  django import forms 
from .models import Trabajador

class superadForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'