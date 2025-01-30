from dataclasses import field
from pyexpat import model
from re import S
from  django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  Trabajador, Permiso, PermisosUsuario, UsuarioRegistrado,SupervisorRegistrado ,PermisosSupervisor, Empresas, EmpresasSupervisores, EmpresasTrabajadores

class SuperadForm(forms.ModelForm):
    class Meta:
        model = SupervisorRegistrado
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    empresa = forms.ModelChoiceField(queryset=Empresas.objects.all(), required=True)

    class Meta:
        model = UsuarioRegistrado
        fields = ['username', 'email', 'first_name', 'last_name', 'permisos', 'empresa']

    def save(self, commit=True):
        usuario_registrado = super().save(commit=False)
        if commit:
            usuario_registrado.save()
            # Asignar permisos al usuario registrado
            for permiso in self.cleaned_data['permisos']:
                PermisosUsuario.objects.create(usuario=usuario_registrado, permiso=permiso)
            # Asignar usuario a la empresa
            EmpresasTrabajadores.objects.create(empresa=self.cleaned_data['empresa'], trabajador=usuario_registrado)
        return usuario_registrado
    




class SupervisorForm(forms.ModelForm):
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    empresa = forms.ModelChoiceField(queryset=Empresas.objects.all(), required=True)

    class Meta:
        model = SupervisorRegistrado
        fields = ['username', 'email', 'first_name', 'last_name', 'permisos', 'empresa']

    def save(self, commit=True):
        supervisor_registrado = super().save(commit=False)
        if commit:
            supervisor_registrado.save()
            # Asignar permisos al supervisor registrado
            for permiso in self.cleaned_data['permisos']:
                PermisosSupervisor.objects.create(supervisor=supervisor_registrado, permiso=permiso)
            # Asignar supervisor a la empresa
            EmpresasSupervisores.objects.create(empresa=self.cleaned_data['empresa'], supervisor=supervisor_registrado)
        return supervisor_registrado
    

class CrearEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['nombre', 'descripcion']

class CrearpermisosForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ['nombre', 'descripcion']

class RelacionarEmpresaSupervisorForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresas.objects.all())
    supervisor = forms.ModelChoiceField(queryset=SupervisorRegistrado.objects.all())

    class Meta:
        model = EmpresasSupervisores
        fields = ['empresa', 'supervisor']

class UsuarioEditForm(forms.ModelForm):
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = UsuarioRegistrado
        fields = ['username', 'email', 'first_name', 'last_name', 'permisos']

class SupervisorForm(forms.ModelForm):
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = SupervisorRegistrado
        fields = ['username', 'email', 'first_name', 'last_name', 'permisos']

class SupervisorEditForm(forms.ModelForm):
    permisos = forms.ModelMultipleChoiceField(
        queryset=Permiso.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = SupervisorRegistrado
        fields = ['username', 'email', 'first_name', 'last_name', 'permisos']


        


    

   