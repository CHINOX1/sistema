from dataclasses import field
from pyexpat import model
from  django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  Trabajador, Permiso, PermisosUsuario, UsuarioRegistrado

class superadForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = UsuarioRegistrado
        fields = ['username', 'email', 'first_name', 'last_name', 'permisos']

    def save(self, commit=True):
        usuario_registrado = super().save(commit=False)
        if commit:
            usuario_registrado.save()
            # Asignar permisos al usuario registrado
            for permiso in self.cleaned_data['permisos']:
                PermisosUsuario.objects.create(usuario=usuario_registrado, permiso=permiso)
        return usuario_registrado
   