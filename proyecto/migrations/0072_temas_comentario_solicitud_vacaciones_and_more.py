# Generated by Django 4.1.1 on 2023-05-06 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0071_solicitud_economicos_comentario_rh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temas_comentario_solicitud_vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(null=True)),
                ('comentario', models.CharField(max_length=30, null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='solicitud_vacaciones',
            old_name='comentario',
            new_name='anexos',
        ),
        migrations.RemoveField(
            model_name='solicitud_economicos',
            name='comentario_rh',
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='asunto',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='estado',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='informacion_adicional',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='recibe_area',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='recibe_nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='recibe_puesto',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='recibe_sector',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Temas_solicitud_vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('tema_comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.temas_comentario_solicitud_vacaciones')),
            ],
        ),
        migrations.AddField(
            model_name='solicitud_vacaciones',
            name='temas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.temas_solicitud_vacaciones'),
        ),
    ]