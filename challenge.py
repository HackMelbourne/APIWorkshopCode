import requests
import base64
TMBD_KEY = 'f3b51c649d284fc47202a5a3e67c458d'
SPOTIFY_CLIENT_ID = '87fd8a956ad845fdb8a3f71547ad1f94'
SPOTIFY_CLIENT_SECRET = 'ec0034846f7749a4880a101b285ea7f3'

def get_trending_movies(type='day', lang='en-US'):

    url = f"https://api.themoviedb.org/3/trending/movie/{type}?language={lang}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2I1MWM2NDlkMjg0ZmM0NzIwMmE1YTNlNjdjNDU4ZCIsInN1YiI6IjY2MmU3N2Y0ZTMzZjgzMDEyMjIxYWI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.me9eMxA4uA55xMH2ZRaiAR66ySFrG_m5Ps_DcLOiDJw"
    }

    response = requests.get(url, headers=headers).json()
    #for debugging purposes
    print("get_tranding_movies")
    return [x['id'] for x in response['results']]

def get_movie_credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2I1MWM2NDlkMjg0ZmM0NzIwMmE1YTNlNjdjNDU4ZCIsInN1YiI6IjY2MmU3N2Y0ZTMzZjgzMDEyMjIxYWI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.me9eMxA4uA55xMH2ZRaiAR66ySFrG_m5Ps_DcLOiDJw"
    }

    response = requests.get(url, headers=headers).json()
    #print(response)
    a = [x['name'] for x in response['crew'] if x["known_for_department"] == 'Sound']
    #for debugging purposes
    print("get_movie_credits")
    return a

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
    #for debugging purposes
    print("get_spotify_req_token")
    return response['access_token']

def search_spotify(bearer, content):

    url = f'https://api.spotify.com/v1/search?q={content}&type=artist&limit=1'
    headers = {
        "Authorization" : "Bearer " + bearer,
        "Content-Type" : "application/json"
    }

    response = requests.get(url, headers=headers).json()
    #for debugging purposes
    print("search_spotify")
    return response['artists']['items'][0]['id']

def get_artist_tracks(bearer,artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    headers = {
        "Authorization" : "Bearer " + bearer,
        "Content-Type" : "application/json"
    }
    response = requests.get(url, headers=headers).json()
    #for debugging purposes
    print("get_artist_tracks")
    return [x['name'] for x in response['tracks'][:1]]

#Part1 populating artists
artists = []
movies = get_trending_movies()
for movie in movies:
    artists.extend(get_movie_credits(movie))
#Part2 finding and populating songs
top_tracks = []
spotify_token = get_spotify_req_token()
#there are too many artists so to save time and space only doing first 5 same can be done for rest of them.
for artist in artists[:5]:
    artist_id = search_spotify(spotify_token, artist)
    top_tracks.extend(get_artist_tracks(spotify_token, artist_id))

print(top_tracks)