# Generated by Django 3.2.18 on 2023-06-06 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctores', '0002_auto_20230605_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.CharField(default='---', max_length=50, verbose_name='Ciudad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='postal',
            field=models.CharField(default='---', max_length=10, verbose_name='Codigo Postal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendario',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Disponible'),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='day',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='dni_doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctores.doctor', verbose_name='DNI Dr'),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='hour',
            field=models.TimeField(verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='id_calendar',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Calendario'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='birthdate',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='dni_dr',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='especiality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctores.especialidad', verbose_name='Especialidad'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='license',
            field=models.IntegerField(default=1, unique=True, verbose_name='Licencia Profesional'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=22, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('X', 'No Binario')], default='M', max_length=1, null=True, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='id_especiality',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID Especialidad'),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='name_especiality',
            field=models.CharField(max_length=50, verbose_name='Especialidad'),
        ),
    ]