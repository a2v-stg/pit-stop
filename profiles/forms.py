from django import forms
from .models import Profile, InterviewFeedback


class ProfileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["file"]


class InterviewFeedbackForm(forms.ModelForm):
    class Meta:
        model = InterviewFeedback
        fields = ["interviewer_name", "score", "comments",
                  "fitment", "decision", "interviewed_for_team"]
        widgets = {
            "fitment": forms.Select(attrs={"class": "form-control"}),
            "score": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 10}),
            "decision": forms.Select(attrs={"class": "form-control"}),
            "interviewed_for_team": forms.Select(attrs={"class": "form-control"}),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["file"]

class ProfileViewForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for __field_name, field in self.fields.items():
            # For text-based fields
            if isinstance(field.widget, (forms.TextInput, forms.Textarea, forms.DateInput, forms.NumberInput, forms.EmailInput)):
                field.widget.attrs.update({
                    'readonly': 'readonly',
                    'class': 'form-control-plaintext',
                    'style': 'background: #f8f9fa; border: none;'
                })

            # For BooleanField (checkbox), disable it
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'disabled': True})

            # For FileField, show the filename instead of the input field
            elif isinstance(field.widget, forms.ClearableFileInput):
                # Disable the file input
                field.widget.attrs.update({'disabled': True})
