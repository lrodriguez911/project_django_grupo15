# Generated by Django 3.2.18 on 2023-06-24 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20230624_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='email',
        ),
    ]
