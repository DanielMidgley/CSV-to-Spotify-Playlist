import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List
import os

class SpotifyPlaylistManager:
    def __init__(self, redirect_uri: str = "http://localhost:8080"):
        """
        Initialize the Spotify client with OAuth authentication.
        
        Args:
            redirect_uri: Redirect URI (must match what's set in your Spotify app)
        """
        
        self.CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
        self.CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
        
        # Define the scope needed to modify playlists
        scope = "playlist-modify-public playlist-modify-private"
        
        # Set up OAuth
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.CLIENT_ID,
            client_secret=self.CLIENT_SECRET,
            redirect_uri=redirect_uri,
            scope=scope
        ))
    
    def add_songs_to_playlist(self, playlist_uri: str, song_uris: List[str]) -> bool:
        """
        Add songs to a specified playlist.
        
        Args:
            playlist_uri: URI of the playlist (e.g., 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M')
            song_uris: List of song URIs to add (e.g., ['spotify:track:4iV5W9uYEdYUVa79Axb7Rh'])
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Extract playlist ID from URI
            playlist_id = self._extract_id_from_uri(playlist_uri)
            
            # Spotify API allows adding up to 100 tracks at once
            # Split into chunks if more than 100 songs
            chunk_size = 100
            for i in range(0, len(song_uris), chunk_size):
                chunk = song_uris[i:i + chunk_size]
                result = self.sp.playlist_add_items(playlist_id, chunk)
                if result and 'snapshot_id' in result:
                    print(f"Added {len(chunk)} songs to playlist. Snapshot ID: {result['snapshot_id']}")
                else:
                    print(f"Added {len(chunk)} songs to playlist.")
            
            print(f"Successfully added {len(song_uris)} songs to playlist!")
            return True
            
        except spotipy.exceptions.SpotifyException as e:
            print(f"Spotify API error: {e}")
            return False
        except Exception as e:
            print(f"Error adding songs to playlist: {e}")
            return False
    
    def _extract_id_from_uri(self, uri: str) -> str:
        """Extract the ID from a Spotify URI."""
        return uri.split(':')[-1]
    
    def add_tracks(self, playlist_uri: str, uris: List[str]) -> bool:
        """
        Convenience method to add tracks to a specific playlist.
        
        Args:
            playlist_uri: URI of the playlist to add tracks to
            uris: List of track URIs to add
            
        Returns:
            bool: True if successful, False otherwise
        """
        success = self.add_songs_to_playlist(playlist_uri, uris)
        if success:
            print("Songs added successfully!")
        return success
