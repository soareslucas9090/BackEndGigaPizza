# Generated by Django 3.2.23 on 2023-12-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maingigapizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcomprado',
            name='is_ativo',
            field=models.BooleanField(default=True),
        ),
    ]
