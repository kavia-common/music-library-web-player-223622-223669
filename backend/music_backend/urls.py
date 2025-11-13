from django.contrib import admin
from django.urls import path, include

# NOTE: This file is retained for backward compatibility.
# The canonical URLConf is config.urls. This mirrors the same routes.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/", include("library.urls")),
]
