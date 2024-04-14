# Generated by Django 4.2.8 on 2024-04-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PersonDonation",
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
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("what_to_donate", models.CharField(max_length=255)),
                ("date", models.DateField()),
            ],
        ),
    ]
