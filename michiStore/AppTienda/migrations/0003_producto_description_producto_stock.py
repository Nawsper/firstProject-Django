# Generated by Django 4.2.1 on 2023-06-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0002_alter_cliente_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='description',
            field=models.TextField(default='Descripción no disponible'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
