from django.urls import path

import profiles.views as profile_views

app_name = "profiles"
urlpatterns = [
    path("", profile_views.index, name="index"),
    path("<str:username>/", profile_views.profile, name="profile"),
]
