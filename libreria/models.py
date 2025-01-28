from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    imagen = models.ImageField(default='user/usuario_defecto.jpg', upload_to='user/', verbose_name='Imagen de perfil')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, verbose_name='Correo electrónico')
    telefono = models.CharField(max_length=20)
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50, null=True, blank=True, verbose_name='Ciudad')
    region = models.CharField(max_length=50, null=True, blank=True, verbose_name='Región')
    direccion = models.CharField(max_length=150,null=True, blank=True, verbose_name='Dirección')

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




class Trabajador(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    rol = models.CharField(max_length=50) 



    def __str__(self):
        fila = self.nombre + ' -- ' + self.rut + ' -- ' + self.rol 
        return fila
   
    