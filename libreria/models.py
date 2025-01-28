from operator import add
from django.db import models
from django.contrib.auth.models import User
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




class Trabajador(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    rol = models.CharField(max_length=50) 



    def __str__(self):
        fila = self.nombre + ' -- ' + self.rut + ' -- ' + self.rol 
        return fila
   
    