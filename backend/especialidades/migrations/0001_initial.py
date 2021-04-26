# Generated by Django 3.2 on 2021-04-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, unique=True, verbose_name='Nome da especialidade')),
            ],
            options={
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
            },
        ),
    ]
