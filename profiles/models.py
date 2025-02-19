from django.db import models


FITMENT_CHOICES = [
    ("good", "Good Fit"),
    ("maybe", "Maybe"),
    ("bad", "Bad Fit"),
]

TEAM_CHOICES = [
    ("backend", "Django Backend"),
    ("frontend", "Vue Frontend"),
    ("nodejs", "Node JS"),
    ("cloud", "Cloud"),
    ("qa", "Quality"),
    ("implementtion", "Implementation"),
    ("automation", "Automation"),
    ("machine_learning", "Deep Tech")
]
DECISION_CHOICES = [
    ("selected", "Selected"),
    ("rejected", "Rejected"),
    ("shortlist", "Shortlisted"),
    ("forward", "Forwarded to next round"),
    ("not_interested","Candidate Not Interested"),
    ("no_decision","Not Decided"),
    ("scheduled","Interview Scheduled")
]

class Profile(models.Model):
    """
    Profile model
    """
    file = models.FileField(upload_to="profiles/")
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    fitment_analysis = models.CharField(
        max_length=20, choices=FITMENT_CHOICES, default="maybe"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=200, blank=True, null=True)
    profile_reviewed = models.BooleanField(default=False)
    profile_contacted = models.BooleanField(default=False)
    interview_scheduled = models.BooleanField(default=False)
    interview_date = models.DateTimeField(null=True, blank=True)
    profile_for_team = models.CharField(
    max_length=20, choices=TEAM_CHOICES, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    decision = models.CharField(max_length=200, blank=True, null=True, default="no_decision", choices=DECISION_CHOICES)

    def __str__(self):
        return self.name if self.name else "Profile"


class InterviewFeedback(models.Model):
    DECISION_CHOICES = [
        
    ]
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="feedbacks")
    interviewer_name = models.CharField(max_length=255)
    score = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)], default=0)
    fitment = models.CharField(
        max_length=20, choices=FITMENT_CHOICES, default="maybe"
    )
    decision = models.CharField(
        max_length=20, choices=DECISION_CHOICES, null=True, blank=True
    )
    comments = models.TextField()
    interviewed_for_team = models.CharField(
        max_length=20, choices=TEAM_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"Feedback for {self.profile.name} by {self.interviewer_name}"
