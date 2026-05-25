import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "279b7060eda2496cb1c7b9661e519e56"
CLIENT_SECRET = "e528de9c14c04776a2ee88c5446fea45"

MOOD_PLAYLISTS = {
    'happy': 'happy upbeat pop',
    'sad': 'sad emotional songs',
    'angry': 'rock intense angry',
    'fear': 'calm ambient relaxing',
    'surprise': 'bollywood party',
    'disgust': 'alternative indie',
    'neutral': 'chill acoustic'
}

def suggest_music(mood):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    ))
    query = MOOD_PLAYLISTS.get(mood.lower(), 'chill music')
    results = sp.search(q=query, type='playlist', limit=5)
    playlists = results['playlists']['items']

    print(f"\nMood detected: {mood}")
    print("Suggested playlists:")
    for i, playlist in enumerate(playlists):
        if playlist is None:
            continue
        spotify_url = (playlist.get('external_urls') or {}).get('spotify', 'URL not available')
        print(f"{i+1}. {playlist['name']} - {spotify_url}")

if __name__ == "__main__":
    for mood in MOOD_PLAYLISTS:
        suggest_music(mood)