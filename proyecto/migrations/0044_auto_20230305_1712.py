# Generated by Django 3.2.3 on 2023-03-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0043_alter_status_fecha_planta'),
    ]

    operations = [
        migrations.AddField(
            model_name='distrito',
            name='division',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='distrito',
            field=models.CharField(max_length=20, null=True),
        ),
    ]