# Generated by Django 4.2.18 on 2025-02-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "profiles",
            "0003_profile_interview_date_profile_interview_scheduled_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
