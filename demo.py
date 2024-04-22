import requests

r = requests.get("https://httpbin.org/get")
print(r)
print(r.json())