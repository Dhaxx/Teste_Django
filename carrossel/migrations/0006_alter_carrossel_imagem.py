# Generated by Django 4.2.8 on 2023-12-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrossel', '0005_alter_carrossel_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrossel',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='carrossel-imgs/%y/%m/'),
        ),
    ]
