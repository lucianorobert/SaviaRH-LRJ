# Generated by Django 4.1.1 on 2022-12-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0026_userdatos_numero_de_trabajador'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvacaciones',
            name='fecha_fin',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='historicalvacaciones',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vacaciones',
            name='fecha_fin',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
    ]