# Generated by Django 4.1.5 on 2023-01-10 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("institutions", "0001_initial"),
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
