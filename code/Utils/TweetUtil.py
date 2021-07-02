from requests_oauthlib import OAuth1Session

import os


class TweetUtil():

    def __init__(self, AT, AS):
        self.CK = os.environ['CK']
        self.CS = os.environ['CS']
        self.AT = AT
        self.AS = AS
        self.session = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
        self.my_twitter_id = 3282531025

    def get_timeline(self):
        url = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=200"
        res = self.session.get(url=url)

        if res.status_code == 200:
            timelines = res.json()
            return timelines
        else:
            print("ERROR : %d" % res.status_code)
        return

    def get_mute_user_reply(self):
        url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=200"
        res = self.session.get(url=url)

        if res.status_code == 200:
            timelines = res.json()
            return timelines
        else:
            print("ERROR : %d" % res.status_code)
        return

    def get_reply(self, keyword, since_id=""):
        url = "https://api.twitter.com/1.1/search/tweets.json"
        params = {'q': keyword, 'count': 200, 'since_id': since_id}  # 取得数
        res = self.session.get(url, params=params)
        if res.status_code == 200:
            timelines = res.json()['statuses']
            return timelines
        else:
            print("ERROR : %d" % res.status_code)
        return

    def excute_reply(self, reply_text, tweet_id):

        url = "https://api.twitter.com/1.1/statuses/update.json"
        params = {"status": reply_text, "in_reply_to_status_id": tweet_id,
                  "auto_populate_reply_metadata": True}

        response = self.session.post(url, params=params)
        if response.status_code == 200:
            print("Succeed!")
        else:
            print("ERROR : %d" % response.status_code)
        return

    def excute_mute(self, user_id):
        url = "https://api.twitter.com/1.1/mutes/users/create.json"
        params = {"user_id": user_id}
        response = self.session.post(url, params=params)
        if response.status_code == 200:
            print("Mute:" + user_id)
        else:
            print("ERROR : %d" % response.status_code)
        return
