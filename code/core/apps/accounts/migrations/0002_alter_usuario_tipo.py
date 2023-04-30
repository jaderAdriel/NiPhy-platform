# Generated by Django 4.2 on 2023-04-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.PositiveSmallIntegerField(choices=[('A', 'Administrador'), ('C', 'Cliente'), ('P', 'Profissional')]),
        ),
    ]