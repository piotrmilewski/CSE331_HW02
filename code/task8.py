import requests

URL = "http://2019shell1.picoctf.com:45158/"

PAYLOAD = {
    'user': "bruh"
}

response = requests.post(url=URL, data=PAYLOAD)

print(response.request.headers.get('Cookie'))
