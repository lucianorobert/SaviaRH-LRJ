# Generated by Django 3.2.3 on 2023-03-13 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0055_alter_perfil_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactorIntegracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.IntegerField(null=True)),
                ('factor', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SalarioDatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UMA', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('Salario_minimo', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='status',
            name='fecha_ingreso',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='PrimaRiesgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prima', models.DecimalField(decimal_places=5, default=0, max_digits=10, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('patronal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.registropatronal')),
            ],
        ),
    ]
