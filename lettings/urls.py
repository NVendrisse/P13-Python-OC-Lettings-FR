from django.urls import path

import lettings.views as letting_views

app_name = "lettings"
urlpatterns = [
    path("", letting_views.index, name="index"),
    path("<int:letting_id>/", letting_views.letting, name="letting"),
]
