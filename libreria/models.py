from enum import unique
from operator import add
from pydoc import describe
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='user/usuario_defecto.jpg', upload_to='user/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Dirección')
    location= models.CharField(max_length=50, null=True, blank=True, verbose_name='Localidad')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Teléfono')
   

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username
   
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class Permiso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True) 
    def __str__(self):
        return self.nombre
    
class PermisosUsuario(models.Model):
    usuario = models.ForeignKey('UsuarioRegistrado', on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'permiso')


class PermisoGrupo(models.Model):
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

    class meta:
        unique_together = ('grupo', 'permiso')

class UsuarioRegistrado(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    permisos = models.ManyToManyField(Permiso, through=PermisosUsuario)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Trabajador(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    rol = models.CharField(max_length=50) 



    def __str__(self):
        fila = self.nombre + ' -- ' + self.rut + ' -- ' + self.rol 
        return fila
   
    