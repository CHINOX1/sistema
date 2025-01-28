
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile


@receiver(post_save, sender=Profile)
def add_to_default_group(sender, instance, created, **kwargs):
    if created:
        try:
            group = Group.objects.get(name='Cliente')
        except Group.DoesNotExist:
            group = Group.objects.create(name='Cliente')        
            group = Group.objects.create(name='admin') 
            group = Group.objects.create(name='trabajador') 

        instance.user.groups.add(group)