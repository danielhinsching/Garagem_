# Generated by Django 5.0.6 on 2024-07-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_marca_rename_descricao_cor_nome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
