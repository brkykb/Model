import spotipy
from respond import respond

from spotipy.oauth2 import SpotifyOAuth

# Spotify API kimlik bilgileri
SPOTIPY_CLIENT_ID = 'd48371b876514cd9bcadb7e956fd098b'
SPOTIPY_CLIENT_SECRET = 'b2b6c23f7dd24c0db673bc411240b34b'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Spotify OAuth yetkilendirme işlemi
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-modify-playback-state"))



def spotifycommand(choose):
    if "pause" in choose.lower() or "stop" in choose.lower():
        sp.pause_playback()
    elif "resume" in choose.lower() or "continue" in choose.lower() or "play" in choose.lower():
        sp.start_playback()
    elif "next" in choose.lower() or "switch" in choose.lower():
        sp.next_track()
    elif "previous" in choose.lower() or "back" in choose.lower():
        sp.previous_track()


    else:
        print("Error: Invalid command")





