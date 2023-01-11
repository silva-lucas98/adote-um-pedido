# Generated by Django 4.1.5 on 2023-01-11 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("institutions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="institution",
            name="owner",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="institution",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
