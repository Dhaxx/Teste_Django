# Generated by Django 4.2.8 on 2023-12-19 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrossel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='globa/images/carrossel-imgs/Y/M/D')),
                ('título', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]