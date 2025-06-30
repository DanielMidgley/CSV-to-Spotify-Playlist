import csv
from track_searcher import URI_finder
from playlist_editor import SpotifyPlaylistManager

def read_csv_tracks(csv_file_path):
    """
    Read track information from a CSV file.
    
    Args:
        csv_file_path: Path to the CSV file containing track name and artist name
        
    Returns:
        List of tuples: [(track_name, artist_name), ...]
    """
    tracks = []
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            # Skip header row if it exists (optional)
            # Uncomment the next line if your CSV has headers
            # next(csv_reader, None)
            
            for row in csv_reader:
                if len(row) >= 2:  # Ensure we have at least track name and artist
                    track_name = row[0].strip()
                    artist_name = row[1].strip()
                    if track_name and artist_name:  # Skip empty rows
                        tracks.append((track_name, artist_name))
                        
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []
    
    return tracks

def get_uris(tracks):
    """
    Get Spotify URIs for a list of tracks.
    
    Args:
        tracks: List of tuples [(track_name, artist_name), ...]
        
    Returns:
        List of Spotify URIs
    """
    uris = []
    uf = URI_finder()
    
    for track in tracks:
        print(f"Searching for: {track[0]} by {track[1]}")
        uri = uf.find_URI(track[0], track[1])
        if uri:
            uris.append(uri)
            print(f"Found: {uri}")
        else:
            print(f"Not found: {track[0]} by {track[1]}")
    
    return uris

def update_playlist(playlist_uri, song_uris):
    """
    Add songs to a Spotify playlist.
    
    Args:
        playlist_uri: Spotify playlist URI
        song_uris: List of Spotify track URIs
    """
    if not song_uris:
        print("No valid URIs to add to playlist.")
        return
        
    playlist_manager = SpotifyPlaylistManager()
    playlist_manager.add_tracks(playlist_uri, song_uris)

def main():
    """
    Main function to read CSV, get URIs, and update playlist.
    """
    # Configuration
    csv_file_path = "songs.csv"  # Change this to your CSV file path
    playlist_uri = "spotify:playlist:YOUR_PLAYLIST_ID"  # Replace with your playlist URI
    
    # Read tracks from CSV
    print("Reading tracks from CSV...")
    tracks = read_csv_tracks(csv_file_path)
    
    if not tracks:
        print("No tracks found in CSV file.")
        return
    
    print(f"Found {len(tracks)} tracks in CSV file.")
    
    # Get URIs for tracks
    print("\nSearching for track URIs...")
    song_uris = get_uris(tracks)
    
    if not song_uris:
        print("No track URIs found.")
        return
    
    print(f"\nFound {len(song_uris)} out of {len(tracks)} tracks.")
    
    # Update playlist
    print("\nUpdating playlist...")
    update_playlist(playlist_uri, song_uris)

if __name__ == "__main__":
    main()