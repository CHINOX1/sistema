from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .models import SupervisorRegistrado, Trabajador, PermisosUsuario,UsuarioRegistrado,Empresas,EmpresasSupervisores,EmpresasTrabajadores,AdminRegistrado,PermisosSupervisor,Permiso
from django.contrib import messages
from .forms import   SupervisorEditForm, UsuarioEditForm, UsuarioForm,SuperadForm,RelacionarEmpresaSupervisorForm,CrearEmpresaForm,SupervisorForm,CrearpermisosForm
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.




def login(request):

    return render(request, 'paginas/login.html')

def login_view(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             auth_login(request, user)
             return redirect('super')
         else:
             return HttpResponse('Credenciales incorrectas')
     return render(request, 'paginas/login.html')


def crear_t(request):
    formulario = superadForm(request.POST or None, request.FILES or None)
    if formulario.is_valid(): #si el formulario es valido
        formulario.save() #guarda el formulario  
        return redirect('superad')# redirige a la pagina superad
    return render(request, 'logins/crear_t.html',{'formulario':formulario})

def superad(request):
    trabajadores = Trabajador.objects.all() 
    print(trabajadores)
   
    return render(request, 'logins/superad.html',{'trabajadores':trabajadores})

def editar_t(request, id):
    usuarioRegistrado = get_object_or_404(UsuarioRegistrado, id=id)
    formulario = UsuarioEditForm(request.POST or None, request.FILES or None, instance=usuarioRegistrado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        # Actualizar la relación con la empresa
        EmpresasTrabajadores.objects.filter(trabajador=usuarioRegistrado).delete()
        empresa = EmpresasTrabajadores.objects.get(trabajador=usuarioRegistrado).empresa
        EmpresasTrabajadores.objects.create(empresa=empresa, trabajador=usuarioRegistrado)
        messages.success(request, 'El trabajador ha sido editado correctamente.')
        return redirect('ver_supervisores_trabajadores', empresa_id=empresa.id)
    return render(request, 'logins/editar/editar_t.html', {'formulario':formulario})

def eliminar_t(request, id):
    usuarioRegistrado = get_object_or_404(UsuarioRegistrado, id=id)
    empresa_id = EmpresasTrabajadores.objects.get(trabajador=usuarioRegistrado).empresa.id
    usuarioRegistrado.delete()
    EmpresasTrabajadores.objects.filter(trabajador=usuarioRegistrado).delete()
    return redirect('ver_supervisores_trabajadores', empresa_id=empresa_id)

def editar_supervisor(request, id):
    supervisorRegistrado = get_object_or_404(SupervisorRegistrado, id=id)
    formulario = SupervisorEditForm(request.POST or None, request.FILES or None, instance=supervisorRegistrado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        # Actualizar la relación con la empresa
        EmpresasSupervisores.objects.filter(supervisor=supervisorRegistrado).delete()
        try:
            empresa = EmpresasSupervisores.objects.get(supervisor=supervisorRegistrado).empresa
        except EmpresasSupervisores.DoesNotExist:
            empresa = None
        if empresa:
            EmpresasSupervisores.objects.create(empresa=empresa, supervisor=supervisorRegistrado)
            messages.success(request, 'El supervisor ha sido editado correctamente.')
            return redirect('ver_supervisores_trabajadores', empresa_id=empresa.id)
        else:
            messages.error(request, 'No se encontró la relación con la empresa.')
            return redirect('ver_supervisores_trabajadores', empresa_id=empresa.id)
    return render(request, 'logins/editar/editar_supervisor.html', {'formulario':formulario})

def eliminar_supervisor(request, id):
    supervisorRegistrado = get_object_or_404(SupervisorRegistrado, id=id)
    empresa_id = EmpresasSupervisores.objects.get(supervisor=supervisorRegistrado).empresa.id
    supervisorRegistrado.delete()
    EmpresasSupervisores.objects.filter(supervisor=supervisorRegistrado).delete()


def pricing (request):
    return render(request, 'paginas/pricing.html')

def base_logins(request):
    return render(request, 'central.html')


def crear_usuario(request, empresa_id):
    empresa = Empresas.objects.get(id=empresa_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario_registrado = form.save(commit=False)
            usuario_registrado.save()
            # Asignar permisos al usuario registrado
            for permiso in form.cleaned_data['permisos']:
                PermisosUsuario.objects.create(usuario=usuario_registrado, permiso=permiso)
            # Asignar usuario a la empresa
            EmpresasTrabajadores.objects.create(empresa=empresa, trabajador=usuario_registrado)
            return redirect('lista_empresas_detalles')
    else:
        form = UsuarioForm()
    return render(request, 'logins/crear_usuario.html', {'form': form, 'empresa': empresa})

def lista_usuarios(request):
    usuarios = UsuarioRegistrado.objects.all()
    usuarios_con_permisos = []
    for usuario in usuarios:
        permisos = PermisosUsuario.objects.filter(usuario=usuario)
        usuarios_con_permisos.append({
            'usuario': usuario,
            'permisos': permisos
        })
    return render(request, 'logins/lista_usuarios.html', {'usuarios_con_permisos': usuarios_con_permisos})

def relacionar_empresa_supervisor(request, empresa_id):
    empresa = Empresas.objects.get(id=empresa_id)
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            supervisor_registrado = form.save(commit=False)
            supervisor_registrado.save()
            # Asignar permisos al supervisor registrado
            for permiso in form.cleaned_data['permisos']:
                PermisosSupervisor.objects.create(supervisor=supervisor_registrado, permiso=permiso)
            # Asignar supervisor a la empresa
            EmpresasSupervisores.objects.create(empresa=empresa, supervisor=supervisor_registrado)
            return redirect('lista_empresas_detalles')
    else:
        form = SupervisorForm()
    return render(request, 'logins/relacionar_empresa_supervisor.html', {'form': form, 'empresa': empresa})

def ver_supervisores_trabajadores(request, empresa_id):
    empresa = Empresas.objects.get(id=empresa_id)
    supervisores = EmpresasSupervisores.objects.filter(empresa=empresa)
    trabajadores = EmpresasTrabajadores.objects.filter(empresa=empresa)
    return render(request, 'logins/ver_supervisores_trabajadores.html', {
        'empresa': empresa,
        'supervisores': supervisores,
        'trabajadores': trabajadores
    })

def crear_empresa(request):
    if request.method == 'POST':
        form = CrearEmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = CrearEmpresaForm()
    return render(request, 'logins/crear_empresa.html', {'form': form})

def lista_empresas(request):
    empresas = Empresas.objects.all()
    return render(request, 'logins/lista_empresas.html', {'empresas': empresas})

def lista_empresas_detalles(request):
    empresas = Empresas.objects.all()
    empresas_detalles = []

    for empresa in empresas:
        num_trabajadores = EmpresasTrabajadores.objects.filter(empresa=empresa).count()
        num_supervisores = EmpresasSupervisores.objects.filter(empresa=empresa).count()
       
        empresas_detalles.append({
            'empresa': empresa,
            'num_trabajadores': num_trabajadores,
            'num_supervisores': num_supervisores,
        })

    return render(request, 'logins/vistas_admin.html', {'empresas_detalles': empresas_detalles})

def eliminar_empresa(request, empresa_id):
    empresa = Empresas.objects.get(id=empresa_id)
    empresa.delete()
    return redirect('lista_empresas_detalles')

def añadir_trabajador(request, empresa_id):
    empresa = Empresas.objects.get(id=empresa_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario_registrado = form.save(commit=False)
            usuario_registrado.save()
            # Asignar permisos al usuario registrado
            for permiso in form.cleaned_data['permisos']:
                PermisosUsuario.objects.create(usuario=usuario_registrado, permiso=permiso)
            # Asignar usuario a la empresa
            EmpresasTrabajadores.objects.create(empresa=empresa, trabajador=usuario_registrado)
            return redirect('lista_empresas_detalles')
    else:
        form = UsuarioForm()
    return render(request, 'logins/crear_usuario.html', {'form': form, 'empresa': empresa})


    pass

def añadir_supervisor(request, empresa_id):
    # Implementa la lógica para añadir un supervisor a la empresa
    pass


def crear_permisos(request):
    if request.method == 'POST':
        form = CrearpermisosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_permisos')
    else:
        form = CrearpermisosForm()
    return render(request, 'permisos/permisos.html', {'form': form})

def lista_permisos(request):
    permisos = Permiso.objects.all()
    return render(request, 'permisos/lista_permisos.html', {'permisos': permisos})