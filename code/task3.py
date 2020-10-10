import requests

URL = "https://2019shell1.picoctf.com/problem/37829/flag"

HEADERS = {
    'User-Agent': 'picobrowser'
}

response = requests.get(url=URL, headers=HEADERS)

data = response.text

flagIndex = data.index('picoCTF{')+8

flag = data[flagIndex:flagIndex+26]

print(flag)
