# Generated by Django 4.2.18 on 2025-02-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_profile_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="decision",
            field=models.CharField(
                blank=True,
                choices=[
                    ("selected", "Selected"),
                    ("rejected", "Rejected"),
                    ("shortlist", "Shortlisted"),
                    ("forward", "Forwarded to next round"),
                    ("not_interested", "Candidate Not Interested"),
                    ("no_decision", "Not Decided"),
                    ("scheduled", "Interview Scheduled"),
                ],
                default="no_decision",
                max_length=200,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="interviewfeedback",
            name="decision",
            field=models.CharField(blank=True, choices=[], max_length=20, null=True),
        ),
    ]
