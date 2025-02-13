from django.contrib import admin
from .models import Profile, InterviewFeedback


class InterviewFeedbackInline(admin.TabularInline):  # Use StackedInline for a vertical format
    model = InterviewFeedback
    extra = 1  # Show one empty form by default

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "uploaded_at")
    search_fields = ("name", "email", "phone")
    inlines = [InterviewFeedbackInline]  # Display feedback inside Profile admin

@admin.register(InterviewFeedback)
class InterviewFeedbackAdmin(admin.ModelAdmin):
    list_display = ("profile", "interviewer_name", "score", "decision")
    list_filter = ("score","decision")
