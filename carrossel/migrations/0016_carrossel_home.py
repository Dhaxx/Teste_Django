# Generated by Django 5.0 on 2023-12-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrossel', '0015_alter_carrossel_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrossel',
            name='home',
            field=models.BooleanField(default=False),
        ),
    ]
