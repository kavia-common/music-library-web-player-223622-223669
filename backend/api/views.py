from django.http import JsonResponse
from django.views.decorators.http import require_GET

# PUBLIC_INTERFACE
@require_GET
def health(request):
    """Simple health check endpoint.

    Returns:
        JsonResponse: {"message": "Server is up!"}
    """
    return JsonResponse({"message": "Server is up!"})
