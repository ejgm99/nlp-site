import json
from apps.logic import twitterAPIKeys as t
from apps.logic import formHandler
from apps.logic.json_manipulation import jsonToHTML

from apps.logic.forms import TopicForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'home/home.html', context)

def get_topic(request):
    return formHandler.formHandler(request, 'name.html', TopicForm, nlpHandler)

def nlpHandler(request):
    nlp_tweets_json = handleTopicFormContent(request)
    j = jsonToHTML(nlp_tweets_json)
    return j

def handleTopicFormContent(request):
    topic = request.POST.get('topic')
    tweets = t.getTopic(topic,5);
    nlp_tweets_json  = t.requestStringPredictions(tweets)
    return json.loads(nlp_tweets_json)
