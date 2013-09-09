import oauth2 as oauth
from settings import TWITTER_DETAILS

class OauthApi():
    def req(self, url, http_method = "GET", post_body = '', http_headers = None):
            consumer = oauth.Consumer(key    = TWITTER_DETAILS['consumer_key'],
                                      secret = TWITTER_DETAILS['consumer_secret'])

            token = oauth.Token(key     = TWITTER_DETAILS['access_token'],
                                secret  = TWITTER_DETAILS['secret'])

            client = oauth.Client(consumer, token)

            resp, content = client.request(
                url,
                method=http_method,
                body=post_body,
                headers=http_headers
            )
            return content