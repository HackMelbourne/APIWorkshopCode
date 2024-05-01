import requests

def create_session():
    req_token = 'f234bc14fadc96066e74f90c6b34c56b2a216f80' #req_tokenx
    print(req_token)
    url = "https://api.themoviedb.org/3/authentication/session/new"

    payload = { "request_token": req_token }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2I1MWM2NDlkMjg0ZmM0NzIwMmE1YTNlNjdjNDU4ZCIsInN1YiI6IjY2MmU3N2Y0ZTMzZjgzMDEyMjIxYWI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.me9eMxA4uA55xMH2ZRaiAR66ySFrG_m5Ps_DcLOiDJw"
    }

    response = requests.post(url, json=payload, headers=headers).json()
    
    print(response)
    return response['session_id']

def create_list(session_id):
    url = f"https://api.themoviedb.org/3/list?session_id={session_id}"
    payload = {
        "name": "Test1.",
        "description": "Just an awesome list.",
        "language": "en"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2I1MWM2NDlkMjg0ZmM0NzIwMmE1YTNlNjdjNDU4ZCIsInN1YiI6IjY2MmU3N2Y0ZTMzZjgzMDEyMjIxYWI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.me9eMxA4uA55xMH2ZRaiAR66ySFrG_m5Ps_DcLOiDJw"
    }
    response = requests.post(url, json=payload, headers=headers).json()

    #print(response)
    return response['list_id']

def add_movie_to_list(list_id, session_id):

    url = f"https://api.themoviedb.org/3/list/{list_id}/add_item?session_id={session_id}"

    payload = { "media_id": 18 }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2I1MWM2NDlkMjg0ZmM0NzIwMmE1YTNlNjdjNDU4ZCIsInN1YiI6IjY2MmU3N2Y0ZTMzZjgzMDEyMjIxYWI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.me9eMxA4uA55xMH2ZRaiAR66ySFrG_m5Ps_DcLOiDJw"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

def delete_list(list_id,session_id):
    url = f"https://api.themoviedb.org/3/list/{list_id}?session_id={session_id}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmM2I1MWM2NDlkMjg0ZmM0NzIwMmE1YTNlNjdjNDU4ZCIsInN1YiI6IjY2MmU3N2Y0ZTMzZjgzMDEyMjIxYWI0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.me9eMxA4uA55xMH2ZRaiAR66ySFrG_m5Ps_DcLOiDJw"
    }
    response = requests.delete(url, headers=headers).json()

    print(response)

session_id = create_session()
list_id = create_list(session_id)
add_movie_to_list(list_id,session_id)
#delete_list(list_id, session_id)