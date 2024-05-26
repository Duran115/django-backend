# Generated by Django 5.0.6 on 2024-05-26 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matricula', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='curso.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matriculas', to='estudiante.estudiante')),
            ],
            options={
                'unique_together': {('estudiante', 'curso')},
            },
        ),
    ]
