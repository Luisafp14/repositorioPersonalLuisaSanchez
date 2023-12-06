# Generated by Django 4.2.4 on 2023-09-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_tallermecanico_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tallermecanico',
            name='atencion',
            field=models.TimeField(null=True, verbose_name='Horario de atencion'),
        ),
        migrations.AddField(
            model_name='tallermecanico',
            name='direction',
            field=models.CharField(max_length=50, null=True, verbose_name='Direccion del taller'),
        ),
    ]