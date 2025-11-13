"""
URL configuration for config project.

- /api/... serves API endpoints (health, tracks, stream)
- /docs and /redoc provide API documentation via drf_yasg
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints (health + library)
    path('api/', include('api.urls')),
    path('api/', include('library.urls')),
]

# Swagger / OpenAPI
schema_view = get_schema_view(
    openapi.Info(
        title="Ocean Music Player API",
        default_version='v1',
        description="API for health, track listing, and streaming",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def get_full_url(request):
    # Respect X-Forwarded-* headers for correct schema base URL behind proxies
    scheme = request.headers.get('X-Forwarded-Proto', request.scheme)
    host = request.headers.get('X-Forwarded-Host', request.get_host())
    forwarded_port = request.headers.get('X-Forwarded-Port')
    if ':' not in host and forwarded_port:
        host = f"{host}:{forwarded_port}"
    return f"{scheme}://{host}"

@csrf_exempt
def dynamic_schema_view(request, *args, **kwargs):
    url = get_full_url(request)
    view = get_schema_view(
        openapi.Info(
            title="Ocean Music Player API",
            default_version='v1',
            description="Interactive API documentation",
        ),
        public=True,
        url=url,
    )
    return view.with_ui('swagger', cache_timeout=0)(request)

urlpatterns += [
    re_path(r'^docs/$', dynamic_schema_view, name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^openapi\.json$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]