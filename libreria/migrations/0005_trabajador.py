# Generated by Django 5.1.5 on 2025-01-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_adminregistrado_empresas_empresassupervisores_and_more'),
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
    ]
