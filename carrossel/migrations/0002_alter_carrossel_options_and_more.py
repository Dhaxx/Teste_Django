# Generated by Django 4.2.8 on 2023-12-19 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrossel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrossel',
            options={'verbose_name_plural': 'carrosseis'},
        ),
        migrations.RenameField(
            model_name='carrossel',
            old_name='título',
            new_name='titulo',
        ),
    ]
