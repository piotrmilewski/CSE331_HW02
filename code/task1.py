import requests

URL = "https://2019shell1.picoctf.com/problem/49886/"

response = requests.get(url=URL)

data = response.text

split1I = data.index('substring(split*2, split*3)')+32
split1 = data[split1I:split1I+4]

split2I = data.index('substring(split*3, split*4)')+32
split2 = data[split2I:split2I+4]

split3I = data.index('substring(split*4, split*5)')+32
split3 = data[split3I:split3I+4]

split4I = data.index('substring(split*5, split*6)')+32
split4 = data[split4I:split4I+4]

split5I = data.index('substring(split*6, split*7)')+32
split5 = data[split5I:split5I+4]

split6I = data.index('substring(split*7, split*8)')+32
split6 = data[split6I:split6I+1]

flag = split1 + split2 + split3 + split4 + split5 + split6

print(flag)
