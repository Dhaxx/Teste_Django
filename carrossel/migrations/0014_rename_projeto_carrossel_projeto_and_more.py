# Generated by Django 5.0 on 2023-12-26 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrossel', '0013_carrossel_projeto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrossel',
            old_name='Projeto',
            new_name='projeto',
        ),
        migrations.RemoveField(
            model_name='carrossel',
            name='servico',
        ),
    ]
