import requests;
import json;
import pandas as pd

s1 = "I decked his ass. Then I cried. I hate killing. It pains me."
s2 = "Then I cried."
s3 = ""
article = u'I killed him. Then I cried. I hate killing. It pains me.'
datastrings = [s1,s2,s3]

def createGetParameters(datastrings):
    print(datastrings)
    param = datastrings[0]
    for string in datastrings[1:]:
        param = param + ",," + string;
    return {"strings":str(param)}

data = createGetParameters(datastrings)
print(data)

r = requests.get('http://localhost:8001/nlp/st/',params =data);
print(r.url)
print(r.text)
content = json.loads(r.text)
d = []
