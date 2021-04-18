# Generated by Django 3.2 on 2021-04-18 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data Disponível')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='medicos.medico', verbose_name='Doutor(a)')),
            ],
            options={
                'verbose_name': 'Disponilidade para Atendimento',
                'verbose_name_plural': 'Disponilidade para Atendimentos',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField(verbose_name='Horário Disponível')),
                ('disponibilidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendas.disponibilidade', verbose_name='Disponibilidade')),
            ],
            options={
                'verbose_name': 'Horário de Atendimento',
                'verbose_name_plural': 'Horários de Atendimento',
            },
        ),
        migrations.AddConstraint(
            model_name='horario',
            constraint=models.UniqueConstraint(fields=('disponibilidade', 'hora'), name='Horário já registrado na agenda'),
        ),
        migrations.AddConstraint(
            model_name='disponibilidade',
            constraint=models.UniqueConstraint(fields=('data', 'medico'), name='Esse(a) Médico(a) já tem uma agenda para esse dia'),
        ),
    ]