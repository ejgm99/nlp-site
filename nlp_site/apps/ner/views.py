from django.shortcuts import render

from apps.logic import twitterAPIKeys as t
from apps.logic import formHandler
from apps.logic.nlp_api_access import requestPrediction
from apps.logic.forms import TopicForm
import emoji
import json
# Create your views here.
def index(request):
    return formHandler.formHandler(request, 'st.html', TopicForm, nerHandler)

def nerHandler(request):
    topic = request.POST.get('topic')
    tweets = t.getTopic(topic,5)
    ner = requestPrediction(tweets,'st')
    ner_json = json.loads(ner)
    for doc in ner_json:
        for token in doc:
            token["score"] = [ emoji.emojize(score , use_aliases = True) for score in token["score"] ]
    payload = combineStringsWithProcessedData(tweets,ner_json)
    return payload

def combineStringsWithProcessedData(strings, data):
    return  [ {"doc":string, "processed":(data[count])} for count,string in enumerate(strings)]
