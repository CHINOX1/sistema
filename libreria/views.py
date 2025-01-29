from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .models import Trabajador, PermisosUsuario,UsuarioRegistrado
from .forms import superadForm, UsuarioForm
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.




def login(request):

    return render(request, 'paginas/login.html')

# [def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('super')
#         else:
#             return HttpResponse('Credenciales incorrectas')
#     return render(request, 'paginas/login.html')]


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

def editar_t(request,id):
    trabajador = Trabajador.objects.get(id=id)
    formulario = superadForm(request.POST or None, request.FILES or None, instance=trabajador)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('superad')
    return render(request, 'logins/editar_t.html',{'formulario':formulario})

def eliminar_t(request,id):
    trabajador = Trabajador.objects.get(id=id)
    trabajador.delete()
    
    return redirect('superad')
def pricing (request):
    return render(request, 'paginas/pricing.html')

def base_logins(request):
    return render(request, 'central.html')


def crear_usuario(request):
    if request.method == 'POST':
        print("Método POST recibido")
        form = UsuarioForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            usuario_registrado = form.save(commit=False)
            usuario_registrado.save()
            # Asignar permisos al usuario registrado
            for permiso in form.cleaned_data['permisos']:
                PermisosUsuario.objects.create(usuario=usuario_registrado, permiso=permiso)
            print("Usuario guardado correctamente")
            return redirect('lista_usuarios')
        else:
            print("Formulario no válido")
            print(form.errors)
    else:
        print("Método GET recibido")
        form = UsuarioForm()
    return render(request, 'logins/crear_usuario.html', {'form': form})

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