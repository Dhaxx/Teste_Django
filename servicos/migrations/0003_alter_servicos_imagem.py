# Generated by Django 4.2.8 on 2023-12-20 23:19

from django.db import migrations, models
import servicos.models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_servicos_options_alter_servicos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=servicos.models.upload_path),
        ),
    ]
