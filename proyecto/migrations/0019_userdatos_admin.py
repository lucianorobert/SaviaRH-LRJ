# Generated by Django 4.1.1 on 2022-12-07 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0018_alter_historicalbonos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatos',
            name='admin',
            field=models.BooleanField(default=False, null=True),
        ),
    ]