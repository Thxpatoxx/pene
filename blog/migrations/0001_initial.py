# Generated by Django 2.0.13 on 2019-05-14 15:14

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
                ('folio', models.PositiveIntegerField()),
                ('estado', models.CharField(choices=[('NO_DISPONIBLE', 'NO_DISPONIBLE'), ('DISPONIBLE', 'DISPONIBLE')], default='DISPONIBLE', max_length=80)),
                ('implemento', models.CharField(choices=[('PALETAS', 'PALETAS'), ('PELOTA_PINPONG', 'PELOTA_PINPONG'), ('PELOTA_FOOTBALL', 'PELOTA_FOOTBALL'), ('PELOTA_BASCKETBALL', 'PELOTA_BASCKETBALL'), ('CANCHA', 'CANCHA')], default='PALETAS', max_length=80)),
            ],
        ),
    ]
