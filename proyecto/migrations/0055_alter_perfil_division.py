# Generated by Django 3.2.3 on 2023-03-06 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0054_perfil_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='division',
            field=models.CharField(blank=True, default='', max_length=15),
            preserve_default=False,
        ),
    ]
