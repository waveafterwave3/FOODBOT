# Generated by Django 5.0 on 2024-03-15 18:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="user",
        ),
    ]
