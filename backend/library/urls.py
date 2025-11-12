from django.urls import path
from . import views

urlpatterns = [
    path("tracks", views.tracks_list, name="tracks_list"),
    path("tracks/<int:track_id>", views.track_detail, name="track_detail"),
    path("stream/<int:track_id>", views.stream_audio, name="stream_audio"),
]
