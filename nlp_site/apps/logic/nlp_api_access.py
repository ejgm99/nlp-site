import requests

def createGetParameters(datastrings):
    print(datastrings)
    param = datastrings[0]
    for string in datastrings[1:]:
        param = param + ",," + string;
    return {"strings":str(param)}


def requestPrediction(data_strings,nlp_model_id):
    data = createGetParameters(data_strings);
    url = 'http://localhost:8001/nlp/'+nlp_model_id+'/'
    print(url)
    r = requests.get(url,params = data)
    print("Requesting with url:",r.url)
    return(r.text)


def requestStringPredictions(data_strings):
    data = createGetParameters(data_strings)
    r = requests.get('http://localhost:8001/nlp/',params = data);
    return r.text;
