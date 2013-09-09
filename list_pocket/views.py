# Create your views here.
from django.http import HttpResponse
from api.twitter import api as twitter

def list_status(request):
    data = twitter.Api().get_list_status('76664096')
    return HttpResponse(data, mimetype="application/json")
