from django.urls import path
from .views import upload_profile, list_profiles, interview_feedback, review_profile, search_profiles, view_profile

urlpatterns = [
    path("upload/", upload_profile, name="upload_profile"),
    path("list/", list_profiles, name="list_profiles"),
    path("feedback/<int:profile_id>/", interview_feedback, name="interview_feedback"),
    path("review/<int:profile_id>/", review_profile, name="review_profile"),
    path("view/<int:profile_id>/", view_profile, name="view_profile"),
    path("search/", search_profiles, name="search_profiles"),
]
