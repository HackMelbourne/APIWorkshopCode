import requests
import base64
import json
SPOTIFY_CLIENT_ID = '87fd8a956ad845fdb8a3f71547ad1f94'
SPOTIFY_CLIENT_SECRET = 'ec0034846f7749a4880a101b285ea7f3'

def get_spotify_req_token():
    url = 'https://accounts.spotify.com/api/token'
    auth = SPOTIFY_CLIENT_ID + ":" + SPOTIFY_CLIENT_SECRET
    encoded_auth = auth.encode("utf-8")
    auth_base64 = str(base64.b64encode(encoded_auth), "utf-8")
    payload = { 
        "grant_type" : "client_credentials"
    }
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers).json()
    #print(response)
    return response['access_token']

def search_spotify(bearer, content):

    url = f'https://api.spotify.com/v1/search?q={content}&type=artist&limit=1'
    headers = {
        "Authorization" : "Bearer " + bearer,
        "Content-Type" : "application/json"
    }

    response = requests.get(url, headers=headers).json()
    #print(response)
    return response['artists']['items'][0]['id']

def get_artist_tracks(bearer,artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    headers = {
        "Authorization" : "Bearer " + bearer,
        "Content-Type" : "application/json"
    }
    response = requests.get(url, headers=headers).json()
    # pretty_response = json.dumps(response, indent=4)
    # print(pretty_response)
    return [x['id'] for x in response['tracks'][:1]]

def get_track(bearer, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {
        "Authorization" : "Bearer " + bearer,
        "Content-Type" : "application/json"
    }
    response = requests.get(url, headers=headers).json()
    return response['album']['name']

spotify_token = get_spotify_req_token()
spotify_artist_id = search_spotify(spotify_token, 'drake')
print(spotify_artist_id)
most_pop_song = get_artist_tracks(spotify_token, spotify_artist_id)
for song in most_pop_song:
    album_name = get_track(spotify_token, song)
    print(album_name)