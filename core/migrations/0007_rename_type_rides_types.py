# Generated by Django 4.1.7 on 2023-04-09 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_rides_status_rides_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rides",
            old_name="type",
            new_name="types",
        ),
    ]
