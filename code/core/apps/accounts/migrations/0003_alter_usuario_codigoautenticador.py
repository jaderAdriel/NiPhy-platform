# Generated by Django 4.2 on 2023-05-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_usuario_codigoautenticador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='codigoAutenticador',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
