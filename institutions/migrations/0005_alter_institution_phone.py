# Generated by Django 4.1.5 on 2023-01-10 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("institutions", "0004_alter_institution_cnpj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="phone",
            field=models.CharField(max_length=16),
        ),
    ]
