# Generated by Django 2.0.13 on 2019-05-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Implementodep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('NO DISPONIBLE', 'NO DISPONIBLE'), ('DISPONIBLE', 'DISPONIBLE')], default='DISPONIBLE', max_length=80)),
                ('implemento', models.CharField(choices=[('PALETAS', 'PALETAS'), ('PELOTA PINPONG', 'PELOTA PINPONG'), ('PELOTA FOOTBALL', 'PELOTA FOOTBALL'), ('PELOTA BASCKETBALL', 'PELOTA BASCKETBALL'), ('CANCHA', 'CANCHA')], default='PALETAS', max_length=80)),
                ('observación', models.TextField(default='Implemento sin detalle', max_length=200)),
            ],
        ),
    ]
