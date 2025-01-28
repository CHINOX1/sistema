# Generated by Django 5.1.5 on 2025-01-28 07:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=10)),
                ('rol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(default='user/usuario_defecto.jpg', upload_to='user/', verbose_name='Imagen de perfil')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ciudad')),
                ('region', models.CharField(blank=True, max_length=50, null=True, verbose_name='Región')),
                ('direccion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirección')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['-id'],
            },
        ),
    ]
