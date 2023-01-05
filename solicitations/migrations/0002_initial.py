# Generated by Django 4.1.5 on 2023-01-04 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("solicitations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="solicitation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="solicitations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
