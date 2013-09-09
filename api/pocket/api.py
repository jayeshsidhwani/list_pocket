import urllib2, json, code
from settings import CONSUMER_KEY, TOKEN_REDIRECT_URI

class Pocket():

    def __init__(self):
        self.consumer_key = CONSUMER_KEY
        self.headers = {'Content-Type' : 'application/json; charset=UTF-8','X-Accept': 'application/json'}

    def get_auth_code(self):
        request_data = json.dumps({"consumer_key": self.consumer_key,
                                   "redirect_uri": TOKEN_REDIRECT_URI})
        url = "https://getpocket.com/v3/oauth/request"
        response = self.make_request(self.headers, request_data, url)
        return "https://getpocket.com/auth/authorize?request_token=%s&redirect_uri=%s?code=%s" %(response['code'], TOKEN_REDIRECT_URI, response['code'])


    def get_request_token(self, auth_code):
        request_data = json.dumps({"consumer_key": self.consumer_key,
                                   "code": auth_code})
        url = "https://getpocket.com/v3/oauth/authorize"
        response_data = self.make_request(self.headers, request_data, url)
        access_code, username = response_data['access_token'],response_data['username']
        return access_code, username

    def make_request(self, headers, data, url):
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return json.load(response)
