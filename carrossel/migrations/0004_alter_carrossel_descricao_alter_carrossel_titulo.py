# Generated by Django 4.2.8 on 2023-12-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrossel', '0003_alter_carrossel_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrossel',
            name='descricao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='carrossel',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
