# Generated by Django 5.1.3 on 2024-12-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tweet", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tweet",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="tweet",
            name="text",
            field=models.CharField(max_length=240),
        ),
    ]
