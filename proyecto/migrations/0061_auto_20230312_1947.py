# Generated by Django 3.2.3 on 2023-03-13 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0060_alter_factorintegracion_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='costo',
            name='laborados',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='historicalcosto',
            name='laborados',
            field=models.IntegerField(default=0, null=True),
        ),
    ]