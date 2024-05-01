import requests

def get_req_token():
    url = "https://api.themoviedb.org/3/authentication/token/new"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "
    }

    response = requests.get(url, headers=headers).json()

    print(response)

get_req_token()