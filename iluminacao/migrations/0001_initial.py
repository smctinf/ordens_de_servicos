# Generated by Django 3.2.17 on 2023-02-07 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('almoxarifado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario_OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=1, null=True, verbose_name='Nível de acesso')),
                ('dt_inclusao', models.DateField(auto_now_add=True, verbose_name='Data de inclusão')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Logradouro')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=130, verbose_name='Nº da OS')),
                ('prioridade', models.CharField(choices=[('0', 'N/D'), ('1', 'Normal'), ('2', 'Urgente')], default='0', max_length=1, null=True, verbose_name='Prioridade')),
                ('dt_solicitacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de solicitação')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('referencia', models.CharField(blank=True, max_length=200, verbose_name='Referência')),
                ('motivo_reclamacao', models.TextField(verbose_name='Motivo da reclamação')),
                ('status', models.CharField(choices=[('0', 'Novo'), ('1', 'Aguardando'), ('2', 'Execução')], default='0', max_length=1, null=True, verbose_name='Status')),
                ('dt_conclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data de conclusão')),
                ('atendente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('contribuinte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Tipo de OS')),
                ('sigla', models.CharField(blank=True, max_length=10, null=True, verbose_name='Sigla')),
            ],
        ),
        migrations.CreateModel(
            name='OS_Linha_Tempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacao.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='OS_ext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_veiculo', models.CharField(blank=True, max_length=14, verbose_name='Código do veículo')),
                ('equipe', models.ManyToManyField(blank=True, null=True, to='iluminacao.Funcionario_OS')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iluminacao.ordemdeservico')),
            ],
        ),
        migrations.AddField(
            model_name='ordemdeservico',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='iluminacao.tipo_os'),
        ),
        migrations.CreateModel(
            name='MateriaisUsados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='almoxarifado.material')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iluminacao.ordemdeservico')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario_os',
            name='tipo_os',
            field=models.ManyToManyField(to='iluminacao.Tipo_OS'),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(blank=True, max_length=200, verbose_name='Referência')),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iluminacao.bairro', verbose_name='Bairro')),
                ('logradouro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='iluminacao.logradouro', verbose_name='Logradouro')),
            ],
        ),
    ]
