# Generated by Django 4.2.4 on 2023-09-14 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cita',
            options={'ordering': ['id'], 'verbose_name': 'Cita', 'verbose_name_plural': 'Citas'},
        ),
        migrations.AlterModelTable(
            name='cita',
            table='Cita',
        ),
    ]