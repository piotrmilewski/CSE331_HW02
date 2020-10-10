import requests
import jsbeautifier

URL = "https://2019shell1.picoctf.com/problem/37886/"

response = requests.get(url=URL)

data = response.text

scriptIndex = data.index('<script type="text/javascript">')+34

script = data[scriptIndex:scriptIndex+1053]

arrayString = script[13:145]
arrayString = arrayString.replace("'", '')
array = arrayString.split(',')

# print(array)

pretty = jsbeautifier.beautify(script)

# print(pretty)

split1 = array[9]

split2 = array[1]

str3 = array[0]
str3 = str3[0:len(str3)-1]
split3 = str3

flag = split1 + split2 + split3

print(flag)
