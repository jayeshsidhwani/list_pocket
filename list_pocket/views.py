# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from api.twitter import api as twitter
from api.twitter import settings
from twython import Twython

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
    return HttpResponse(authorized_tokens, mimetype="application/json")


    # try:
    #     profile = TwitterProfile.objects.get(screen_name = authorized_tokens['screen_name'])
    #     user = User.objects.get(pk=profile.user_id)
    #     user.backend = 'django.contrib.auth.backends.ModelBackend'
    #
    #     if user.is_active:
    #         auth_login(request, user)
    #         return HttpResponseRedirect(reverse('app_name:url_name'))
    #     else:
    #         return HttpResponseRedirect(reverse('app_name:login'))
    # except TwitterProfile.DoesNotExist:
    #     screen_name = authorized_tokens['screen_name']
    #     oauth_token = authorized_tokens['oauth_token']
    #     oauth_token_secret = authorized_tokens['oauth_token_secret']

