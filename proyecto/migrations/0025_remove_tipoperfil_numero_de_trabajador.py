# Generated by Django 4.1.1 on 2022-12-12 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0024_tipoperfil_numero_de_trabajador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoperfil',
            name='numero_de_trabajador',
        ),
    ]
