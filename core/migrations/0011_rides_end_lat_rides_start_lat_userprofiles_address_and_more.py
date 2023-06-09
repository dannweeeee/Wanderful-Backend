# Generated by Django 4.1.7 on 2023-04-09 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0010_remove_riderequests_accepted_riderequests_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="rides",
            name="end_lat",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="rides",
            name="start_lat",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="userprofiles",
            name="address",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="userprofiles",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="rides",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
