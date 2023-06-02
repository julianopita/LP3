# Generated by Django 4.2 on 2023-04-27 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tabela_alter_cliente_options_alter_marca_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rotativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(verbose_name='Entrada')),
                ('saida', models.DateTimeField(blank=True, null=True, verbose_name='Saida')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('pago', models.BooleanField(default=False, verbose_name='Pago')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observacoes')),
                ('id_tabela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tabela', verbose_name='Valor')),
                ('id_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo', verbose_name='Veiculo')),
            ],
            options={
                'verbose_name_plural': 'Rotativo',
            },
        ),
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observacoes')),
                ('id_tabela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tabela', verbose_name='Valor')),
                ('id_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo', verbose_name='Veiculo')),
            ],
            options={
                'verbose_name_plural': 'Mensalistas',
            },
        ),
    ]