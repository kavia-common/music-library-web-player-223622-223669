# Ocean Music Player Backend (Django)

Simple Django API serving music tracks and a streaming proxy.

## Endpoints

- GET /api/tracks — list of tracks
- GET /api/tracks/<id> — track details
- GET /api/stream/<id> — audio stream proxy for a given track

## Setup

1. Create and activate a virtual environment
   python -m venv .venv
   . .venv/bin/activate  # Windows: .venv\\Scripts\\activate

2. Install dependencies
   pip install -r requirements.txt

3. Run migrations (SQLite, no models in this prototype)
   python manage.py migrate

4. Start server
   python manage.py runserver 0.0.0.0:3001

Frontend will call http://localhost:3001 by default.

## CORS

Allowed origins default to http://localhost:3000. Override by setting FRONTEND_URL env:

FRONTEND_URL=https://your-frontend-url.example

## Notes

- The app uses public-domain sample tracks (Bensound). Replace with your own by editing library/views.py SAMPLE_TRACKS.
