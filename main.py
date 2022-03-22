####################################### Package Imports #######################################



import os
import sys
import requests
import json
from json.decoder import JSONDecodeError
from dotenv import load_dotenv
import webbrowser
import spotipy
import spotipy.util as util
from spotipy import Spotify as sp
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


####################################### Env Setup #######################################

sys.path.insert(0, os.environ['HOME'])

dotenv_path = os.environ['HOME'] + '/prod.env'

load_dotenv(dotenv_path, override=True)    
locals().update(os.environ)
scope = 'user-read-private user-read-playback-state user-library-read user-read-recently-played'

####################################### Main #######################################
# scope = "playlist-read-private playlist-modify-private playlist-modify-public playlist-modify-public"
# client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# print(sp.current_user_saved_tracks())
username = '1215542086'  
redirect_uri = 'http://localhost:8888/callback/ '                                    
# try:
#     token = util.prompt_for_user_token(username, scope)
# except (AttributeError, JSONDecodeError):
#     os.remove(f".cache-{username}")
#     token = util.prompt_for_user_token(username, scope)

scope = "user-library-read"

token = util.prompt_for_user_token(
username,
scope,
client_id=spotify_client_id,
client_secret=spotify_client_secret,
redirect_uri=redirect_uri,
)


spotify = spotipy.Spotify(auth=token)
results = spotify.current_user_saved_tracks()
print(type(results)
# top_track = spotify.current_user_top_tracks(limit=50, time_range='medium_term')
# print(top_track)
# scope = "user-library-read"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id , client_secret=spotify_client_secret,redirect_uri='http://localhost:8080/callback', scope=scope, open_browser=False))
# print(sp)
# current_user_object = sp.current_user()
# current_user_id = current_user_object['id']
# print(current_user_object)

# username = '1215542086'
# # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username,
# #                                                client_id=spotify_client_id, 
# #                                                client_secret=spotify_client_secret, 
# #                                                scope=scope,
# #                                                redirect_uri='http://localhost:8888/callback/'))

# # user = sp.user("1215542086")
# # print(user)
# token_url = "https://accounts.spotify.com/api/token"
# method = "POST"
# token_data = {
#     "grant_type": "client_credentials"
# }
# token_header = {
#     "Authorization: "
# }
# resp = requests.get()
# # - get token from auth request