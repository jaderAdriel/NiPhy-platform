# Generated by Django 4.2 on 2023-07-10 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Consulta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.CharField(max_length=255)),
                ('consulta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='prontuario', to='Consulta.consulta')),
            ],
        ),
    ]
