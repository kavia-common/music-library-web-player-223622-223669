from django.http import JsonResponse, StreamingHttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
import requests

# Sample public-domain/placeholder audio sources
SAMPLE_TRACKS = [
    {
        "id": 1,
        "title": "Acoustic Breeze",
        "artist": "Bensound",
        "duration": 213,
        "url": "https://www.bensound.com/bensound-music/bensound-acousticbreeze.mp3",
    },
    {
        "id": 2,
        "title": "Creative Minds",
        "artist": "Bensound",
        "duration": 287,
        "url": "https://www.bensound.com/bensound-music/bensound-creativeminds.mp3",
    },
    {
        "id": 3,
        "title": "Sunny",
        "artist": "Bensound",
        "duration": 122,
        "url": "https://www.bensound.com/bensound-music/bensound-sunny.mp3",
    },
]

def _find_track(track_id: int):
    for t in SAMPLE_TRACKS:
        if t["id"] == track_id:
            return t
    return None

"""Views for the music library API providing track listing, details, and streaming."""

# PUBLIC_INTERFACE
@require_GET
@csrf_exempt
def tracks_list(request):
    """List tracks endpoint.

    PUBLIC: GET /api/tracks
    Returns:
        JsonResponse: JSON array of tracks [{id, title, artist, duration, url}]
    """
    return JsonResponse(SAMPLE_TRACKS, safe=False)

# PUBLIC_INTERFACE
@require_GET
@csrf_exempt
def track_detail(request, track_id: int):
    """Track details by id endpoint.

    PUBLIC: GET /api/tracks/<id>
    Args:
        track_id (int): Track identifier
    Returns:
        JsonResponse: Track object or 404 JSON error
    """
    t = _find_track(track_id)
    if not t:
        # Return a proper JSON 404 response
        return JsonResponse({"error": "Not found"}, status=404)
    return JsonResponse(t)

# PUBLIC_INTERFACE
@require_GET
@csrf_exempt
def stream_audio(request, track_id: int):
    """Proxy stream endpoint for a track.

    PUBLIC: GET /api/stream/<id>
    Streams bytes from the remote URL so frontend can use backend origin.

    Args:
        track_id (int): Track identifier
    Returns:
        StreamingHttpResponse: Proxied audio stream with appropriate headers
    """
    t = _find_track(track_id)
    if not t:
        return HttpResponseNotFound("Not found")
    src = t.get("url")
    try:
        upstream = requests.get(src, stream=True, timeout=10)
        content_type = upstream.headers.get("Content-Type", "audio/mpeg")
        resp = StreamingHttpResponse(
            streaming_content=upstream.iter_content(chunk_size=64 * 1024),
            content_type=content_type,
            status=upstream.status_code,
        )
        # Basic passthrough of length if available
        if upstream.headers.get("Content-Length"):
            resp["Content-Length"] = upstream.headers["Content-Length"]
        # Hint to clients that range requests are acceptable
        resp["Accept-Ranges"] = "bytes"
        return resp
    except requests.RequestException:
        return HttpResponseNotFound("Source unavailable")
