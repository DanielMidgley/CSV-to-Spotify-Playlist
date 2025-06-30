import requests
import base64
import os

class URI_finder:
    def __init__(self):
        self.CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
        self.CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

        if not self.CLIENT_ID or not self.CLIENT_SECRET:
            raise ValueError("SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET must be set as environment variables.")

    def get_access_token(self, client_id, client_secret):
        auth_str = f"{client_id}:{client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

        headers = {
            "Authorization": f"Basic {b64_auth_str}"
        }
        data = {
            "grant_type": "client_credentials"
        }

        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def search_track_uri(self, track_title, artist_name, access_token):
        query = f"track:{track_title} artist:{artist_name}"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        params = {
            "q": query,
            "type": "track",
            "limit": 1
        }

        response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
        response.raise_for_status()
        results = response.json()
        items = results.get("tracks", {}).get("items", [])

        if items:
            track = items[0]
            return track["uri"]
        else:
            return None
        
    def find_URI(self, title: str, artist: str):
        title = "Shape of You"
        artist = "Ed Sheeran"

        token = self.get_access_token(self.CLIENT_ID, self.CLIENT_SECRET)
        uri = self.search_track_uri(title, artist, token)

        if uri:
            return uri
        return None
