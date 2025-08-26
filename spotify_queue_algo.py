
# Spotify Playlist Algorithm with Spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import random

# Replace these with your credentials
#Comment this out or put into environment variables for security
CLIENT_ID = 'ENTER CREDS HERE'
CLIENT_SECRET = 'ENTER CREDS HERE'
REDIRECT_URI = 'ENTER CREDS HERE'
PLAYLIST_ID = 'ENTER CREDS HERE'

# Authenticate and create Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-read-private user-library-read user-read-currently-playing"
))


def fetch_playlist():
    results = sp.playlist_items(PLAYLIST_ID, additional_types=['track'])
    tracks = results['items']
    playlist = []
    for item in tracks:
        track = item['track']
        title = track['name']
        popularity = track['popularity']
        artist_name = track['artists'][0]['name']
        artist_id = track['artists'][0]['id']
        artist_info = sp.artist(artist_id)
        genres = artist_info['genres'] if artist_info['genres'] else ['Unknown']
        playlist.append({
            "title": title,
            "artist": artist_name,
            "popularity": popularity,
            "genres": genres
        })
    return playlist

def recommend_next_song(current_song, playlist):
    # Recommend a song with similar genre, not the current song
    current_genres = set(current_song['genres'])
    candidates = [song for song in playlist if song != current_song and any(g in current_genres for g in song['genres'])]
    if candidates:
        return random.choice(candidates)
    else:
        # Fallback: recommend any other song
        return random.choice([song for song in playlist if song != current_song])


def get_currently_playing():
    current = sp.current_user_playing_track()
    if current and current.get('item'):
        track = current['item']
        title = track['name']
        artist_name = track['artists'][0]['name']
        return title, artist_name
    return None, None

def main_loop():
    print("Monitoring your Spotify playback...")
    playlist = fetch_playlist()
    last_song = None
    while True:
        title, artist = get_currently_playing()
        if title and artist:
            if last_song != (title, artist):
                print(f"Now playing: {title} by {artist}")
                # Find song in playlist
                current_song = next((s for s in playlist if s['title'] == title and s['artist'] == artist), None)
                if current_song:
                    next_song = recommend_next_song(current_song, playlist)
                    print(f"Next recommended song: {next_song['title']} by {next_song['artist']} (Genres: {', '.join(next_song['genres'])})\n")
                else:
                    print("Current song not found in playlist.\n")
                last_song = (title, artist)
        else:
            print("No song currently playing.")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    while True:
        main_loop()
