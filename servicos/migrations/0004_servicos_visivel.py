# Generated by Django 4.2.8 on 2023-12-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_alter_servicos_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='visivel',
            field=models.BooleanField(default=True),
        ),
    ]
