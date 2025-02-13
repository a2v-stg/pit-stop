from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, InterviewFeedback
from .forms import ProfileUploadForm, InterviewFeedbackForm, ProfileEditForm
from .utils import process_profile

def upload_profile(request):
    if request.method == "POST":
        form = ProfileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
            extracted_data = process_profile(profile.file.path)
            Profile.objects.filter(id=profile.id).update(**extracted_data)
            return redirect("review_profile", profile.id)
        else:
            print("Form Errors:", form.errors)  # Debugging
    else:
        form = ProfileUploadForm()
    return render(request, "profiles/upload.html", {"form": form})

def list_profiles(request):
    profiles = Profile.objects.all()
    return render(request, "profiles/list.html", {"profiles": profiles})

def interview_feedback(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == "POST":
        form = InterviewFeedbackForm(request.POST)
        print(form)

        if form.is_valid():
            print(form)
            feedback = form.save(commit=False)
            feedback.profile = profile
            feedback.save()
            return redirect("list_profiles")
    else:
        form = InterviewFeedbackForm()
    return render(request, "profiles/feedback.html", {"form": form, "profile": profile})

def review_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("list_profiles")
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, "profiles/review.html", {"form": form, "profile": profile})

def search_profiles(request):
    query = request.GET.get("q", "").strip()
    profiles = Profile.objects.none()  # Don't fetch any profiles by default

    if query:
        profiles = Profile.objects.filter(
            name__icontains=query
        ) | Profile.objects.filter(
            email__icontains=query
        ) | Profile.objects.filter(
            phone__icontains=query
        )

    return render(request, "profiles/search_profiles.html", {"profiles": profiles, "query": query})

