# Generated by Django 3.2.16 on 2023-01-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iluminacao', '0005_rename_equipe_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do funcionário'),
        ),
    ]
