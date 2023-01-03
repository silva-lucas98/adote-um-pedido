# Generated by Django 4.1.5 on 2023-01-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("state", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("street", models.CharField(max_length=255)),
                ("number", models.IntegerField()),
                ("district", models.CharField(max_length=255)),
                ("zip_code", models.IntegerField()),
            ],
        ),
    ]
