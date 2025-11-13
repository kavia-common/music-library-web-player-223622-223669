from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Health and additional API endpoints
    path("api/", include("api.urls")),
    # Music library endpoints
    path("api/", include("library.urls")),
]
