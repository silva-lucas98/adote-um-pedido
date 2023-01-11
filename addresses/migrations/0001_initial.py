# Generated by Django 4.1.5 on 2023-01-11 15:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("state", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=50)),
                ("number", models.CharField(max_length=16)),
                ("district", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=8)),
            ],
        ),
    ]
