from django import forms
from .models import Profile, InterviewFeedback

class ProfileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["file"]

class InterviewFeedbackForm(forms.ModelForm):
    class Meta:
        model = InterviewFeedback
        fields = ["interviewer_name", "score", "comments","fitment","decision","interviewed_for_team"]
        widgets = {
            "fitment": forms.Select(attrs={"class": "form-control"}),  
            "score": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 10}),  
            "decision": forms.Select(attrs={"class": "form-control"}),  
            "interviewed_for_team": forms.Select(attrs={"class": "form-control"}),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email", "phone", "profile_url", "skills", "summary", "fitment_analysis"]