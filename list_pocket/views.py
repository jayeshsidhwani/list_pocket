# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from api.twitter import api as twitter
from api.twitter import settings
from twython import Twython
from models import Users

def home(request):
    return render_to_response('home/index.html')

def list_status(request):
    data = twitter.Api().get_list_status('76664096')
    return HttpResponse(data, mimetype="application/json")

def twitter_login(request):
    twitter = Twython(
        app_key = settings.TWITTER_DETAILS['consumer_key'],
        app_secret = settings.TWITTER_DETAILS['consumer_secret']
    )
    auth_props = twitter.get_authentication_tokens()
    request.session['request_token'] = auth_props

    return HttpResponseRedirect(auth_props['auth_url'])


def twitter_callback(request):

    twitter = Twython(
        app_key = settings.TWITTER_DETAILS['consumer_key'],
        app_secret = settings.TWITTER_DETAILS['consumer_secret'],
        oauth_token = request.session['request_token']['oauth_token'],
        oauth_token_secret = request.session['request_token']['oauth_token_secret']
    )

    oauth_verifier = request.GET['oauth_verifier']
    authorized_tokens = twitter.get_authorized_tokens(oauth_verifier)

    user_data = { 'twitter_id': authorized_tokens['user_id'],
                  'twitter_handle': authorized_tokens['screen_name'],
                  'twitter_token': authorized_tokens['oauth_token'] }

    Users.objects.get_or_create(**user_data)
    request.session['user_id'] = authorized_tokens['user_id']

    return HttpResponseRedirect('/dashboard')

def dashboard(request):
    return HttpResponse(request.session['user_id'])
