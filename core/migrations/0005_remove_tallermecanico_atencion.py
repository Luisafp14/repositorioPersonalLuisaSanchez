# Generated by Django 4.2.4 on 2023-09-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tallermecanico_atencion_tallermecanico_direction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tallermecanico',
            name='atencion',
        ),
    ]
