# Generated by Django 5.0 on 2024-02-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0010_alter_projetos_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(default='Sales', max_length=50),
        ),
    ]