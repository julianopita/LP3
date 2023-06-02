# Generated by Django 4.2 on 2023-05-12 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rotativo_mensalista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='marca_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca', verbose_name='Fabricante'),
        ),
    ]