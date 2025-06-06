# Generated by Django 5.1.3 on 2025-04-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="db",
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
                ("historical_yield", models.FloatField(null=True)),
                ("rainfall", models.FloatField(null=True)),
                ("humidity", models.FloatField(null=True)),
                ("soil_ph", models.FloatField(null=True)),
                ("organic_content", models.FloatField(null=True)),
                ("predicted_yield", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
