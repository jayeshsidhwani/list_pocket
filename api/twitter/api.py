import json, code
from oauth_api import OauthApi


class Api(object):

    def get_list_status(self, list_id):
        print "Getting lists"
        request_url = "https://api.twitter.com/1.1/lists/statuses.json?list_id=%s" %list_id
        response = json.loads(OauthApi().req(url = request_url))
        return response
