import requests

localhost ='http://localhost:8001/nlp/'
aws = 'http://ec2-3-136-18-160.us-east-2.compute.amazonaws.com/nlp/'

def createGetParameters(datastrings):
    print(datastrings)
    param = datastrings[0]
    for string in datastrings[1:]:
        param = param + ",," + string;
    return {"strings":str(param)}


def requestPrediction(data_strings,nlp_model_id):
    data = createGetParameters(data_strings);
    url = aws+nlp_model_id+'/'
    print(url)
    r = requests.get(url,params = data)
    print("Requesting with url:",r.url)
    return(r.text)


def requestStringPredictions(data_strings):
    data = createGetParameters(data_strings)
    r = requests.get('http://localhost:8001/nlp/',params = data);
    return r.text;
