# Generated by Django 3.2.14 on 2022-11-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iluminacao', '0002_tipo_os_sigla'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemdeservico',
            name='prioridade',
            field=models.CharField(choices=[('0', 'Normal'), ('1', 'Urgente')], max_length=1, null=True, verbose_name='Prioridae'),
        ),
        migrations.AddField(
            model_name='ordemdeservico',
            name='status',
            field=models.CharField(choices=[('0', 'NOVO'), ('1', 'EXECUÇÃO')], max_length=1, null=True, verbose_name='Status'),
        ),
    ]