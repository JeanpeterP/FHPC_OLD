# Generated by Django 4.1.7 on 2023-02-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_account_account_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="pet_number",
            field=models.PositiveIntegerField(default=3214, unique=True),
            preserve_default=False,
        ),
    ]
