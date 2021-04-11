# Generated by Django 3.2 on 2021-04-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='crm',
            field=models.CharField(max_length=64, unique=True, verbose_name='CRM'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(to='specialties.Specialty', verbose_name='Especialidades'),
        ),
    ]