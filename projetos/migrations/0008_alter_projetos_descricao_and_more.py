# Generated by Django 5.0 on 2024-01-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0007_alter_projetos_descricao_alter_projetos_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='servicos_realizados',
            field=models.TextField(blank=True, null=True),
        ),
    ]
