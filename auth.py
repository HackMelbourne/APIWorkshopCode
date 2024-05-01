import requests

def get_req_token():
    url = "https://api.themoviedb.org/3/authentication/token/new"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2I1MWM2NDlkMjg0ZmM0NzIwMmE1YTNlNjdjNDU4ZCIsInN1YiI6IjY2MmU3N2Y0ZTMzZjgzMDEyMjIxYWI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.me9eMxA4uA55xMH2ZRaiAR66ySFrG_m5Ps_DcLOiDJw"
    }

    response = requests.get(url, headers=headers).json()

    print(response)

get_req_token()