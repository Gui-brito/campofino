# Generated by Django 3.0.4 on 2020-03-23 23:46

from django.db import migrations, models
import personal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_name', models.CharField(max_length=32, verbose_name='Nome do Produto')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição do Produto')),
                ('status', models.BooleanField(default=True, verbose_name='Status do Produto')),
                ('data_insercao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Inserção')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=personal.models.local_upload, verbose_name='Imagem do Produto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': '(01) - Produtos',
            },
        ),
    ]