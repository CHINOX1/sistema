from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .models import Trabajador
from .forms import superadForm
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
    return render(request, 'logins/base_logins.html')