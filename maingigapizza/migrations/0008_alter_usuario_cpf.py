# Generated by Django 3.2.23 on 2023-12-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maingigapizza', '0007_usuario_is_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]