# **Spotify Playlist Algorithm**

This Python script uses the Spotify API to monitor your currently playing song and recommends the next song from your playlist based on genre similarity.

---

## **Features**

- 🎵 Monitors your Spotify playback in real time  
- 🎶 Recommends the next song from your playlist based on genre  
- 🐍 Uses Spotipy (Python Spotify API library)

---

## **Setup**

**1. Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/Spotify-Algorithm.git
cd Spotify-Algorithm
```

**2. Install dependencies:**
```bash
pip install spotipy
```

**3. Spotify Developer Setup:**
- Create a Spotify Developer App at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
- Add your Spotify account to the app’s user management.
- Set your Redirect URI to `http://127.0.0.1:8888/callback`.
- Copy your `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI` into `spotify_queue_algorithm.py`.

**4. Edit your credentials in `spotify_queue_algorithm.py`:**
```python
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'
PLAYLIST_ID = 'your_playlist_id'
```

---

## **Usage**

1. Start playing a song on your Spotify account.
2. Run the script:
   ```bash
   python spotify_queue_algorithm.py
   ```
3. The script will monitor your playback and recommend the next song.

---

## **Security**

- **Do not share your client secret publicly.**  
  Consider using environment variables for credentials in production.
