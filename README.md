# CSV-to-Spotify-Playlist

A Python application that reads song titles and artists from a CSV file and automatically adds them to a Spotify playlist.

## Features

- Read track information from CSV files
- Search for tracks on Spotify using the Spotify Web API
- Automatically add found tracks to specified playlists
- Handles batch additions (up to 100 tracks per API call)
- Error handling for missing tracks and API issues

## Prerequisites

- Python 3.6 or higher
- A Spotify account
- Spotify Developer App credentials

## Installation

1. Clone this repository:
```bash
git clone https://github.com/DanielMidgley/CSV-to-Spotify-Playlist.git
cd CSV-to-Spotify-Playlist
```

2. Install required dependencies:
```bash
pip install spotipy requests
```

## Spotify API Setup

### 1. Create a Spotify Developer App

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click "Create App"
4. Fill in the required fields:
   - **App Name**: Choose any name (e.g., "CSV Playlist Manager")
   - **App Description**: Brief description of your app
   - **Redirect URI**: `http://localhost:8080`
   - **Website**: Can be left blank or use a placeholder
5. Accept the terms and create the app

### 2. Get Your API Credentials

1. In your newly created app dashboard, click "Settings"
2. Note down your **Client ID** and **Client Secret**
3. Make sure the Redirect URI is set to `http://localhost:8080`

### 3. Set Environment Variables

Create environment variables for your API credentials. The method depends on your operating system:

#### Windows (Command Prompt):
```cmd
set SPOTIFY_CLIENT_ID=your_client_id_here
set SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

#### Windows (PowerShell):
```powershell
$env:SPOTIFY_CLIENT_ID="your_client_id_here"
$env:SPOTIFY_CLIENT_SECRET="your_client_secret_here"
```

#### macOS/Linux:
```bash
export SPOTIFY_CLIENT_ID="your_client_id_here"
export SPOTIFY_CLIENT_SECRET="your_client_secret_here"
```

## Usage

### 1. Prepare Your CSV File

Create a CSV file with track names and artists. The format should be:
```csv
track_name,artist_name
Shape of You,Ed Sheeran
Blinding Lights,The Weeknd
Watermelon Sugar,Harry Styles
```

**Important**: 
- The first column should contain track names
- The second column should contain artist names
- No header row is required (but if you have one, uncomment the header skip line in the code)

### 2. Get Your Playlist URI

1. Open Spotify and navigate to the playlist you want to add songs to
2. Click the three dots menu (⋯) next to the playlist name
3. Select "Share" → "Copy link to playlist"
4. The URI format is: `spotify:playlist:PLAYLIST_ID`
   
   If you copied a link like `https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M`, the URI would be `spotify:playlist:37i9dQZF1DXcBWIGoYBM5M`

### 3. Configure and Run

1. Open `app.py` and update the configuration:
```python
csv_file_path = "your_songs.csv"  # Path to your CSV file
playlist_uri = "spotify:playlist:YOUR_PLAYLIST_ID"  # Your playlist URI
```

2. Run the application:
```bash
python app.py
```

### 4. Authentication

On first run, the application will:
1. Open your web browser for Spotify authentication
2. Ask you to log in and authorize the app
3. Redirect to a localhost page (this may show an error, but that's normal)
4. Copy the full URL from your browser and paste it into the terminal when prompted

## File Structure

```
├── app.py                  # Main application script
├── playlist_editor.py      # Spotify playlist management
├── track_searcher.py       # Track URI search functionality
├── songs.csv               # Your CSV file (create this)
└── README.md               # This file
```

## Example Output

```
Reading tracks from CSV...
Found 3 tracks in CSV file.

Searching for track URIs...
Searching for: Shape of You by Ed Sheeran
Found: spotify:track:7qiZfU4dY1lWllzX7mPBI3
Searching for: Blinding Lights by The Weeknd
Found: spotify:track:0VjIjW4GlUZAMYd2vXMi3b
Searching for: Watermelon Sugar by Harry Styles
Found: spotify:track:6UelLqGlWMcVH1E5c4H7lY

Found 3 out of 3 tracks.

Updating playlist...
Added 3 songs to playlist. Snapshot ID: ABC123...
Successfully added 3 songs to playlist!
Songs added successfully!
```

## Troubleshooting

### Common Issues

1. **Environment variables not found**: Make sure you've set the `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` environment variables correctly.

2. **Authentication errors**: Ensure your Redirect URI in the Spotify app settings matches `http://localhost:8080`.

3. **Tracks not found**: The search uses exact matching. Try variations of artist/track names if songs aren't found.

4. **Permission errors**: Make sure you have permission to modify the target playlist (you should be the owner or have collaborative access).

### Error Messages

- `SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET must be set as environment variables`: Set up your environment variables as described above.
- `CSV file not found`: Check that your CSV file path is correct.
- `No tracks found in CSV file`: Verify your CSV format and that it contains data.

## Requirements

- `spotipy>=2.22.1`
- `requests>=2.31.0`

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Feel free to submit issues and enhancement requests!
