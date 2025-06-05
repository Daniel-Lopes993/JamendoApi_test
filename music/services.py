# music/services.py
import requests
from django.conf import settings

JAMENDO_API_URL = 'https://api.jamendo.com/v3.0'
CLIENT_ID = getattr(settings, 'JAMENDO_CLIENT_ID', 'YOUR_CLIENT_ID')

def get_top_artists(limit=10):
    url = f"{JAMENDO_API_URL}/artists"
    params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'limit': limit,
        'order': 'popularity_total'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_top_tracks(limit=10):
    url = f"{JAMENDO_API_URL}/tracks"
    params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'limit': limit,
        'order': 'popularity_total'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_track_info(track_id):
    url = f"{JAMENDO_API_URL}/tracks"
    params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'id': track_id
    }
    response = requests.get(url, params=params)
    return response.json()
