import requests;
import json;

s1 = "this is bad"
s2 = "this is good"
s3 = "this is neutral"

datastrings = [s1,s2,s3]

def createGetParameters(datastrings):
    print(datastrings)
    param = datastrings[0]
    for string in datastrings:
        param = param + ",," + string;
    return {"strings":str(param)}

data = createGetParameters(datastrings)
print(data)

r = requests.get('http://localhost:8001/nlp/',params =data);
print(r.url)
