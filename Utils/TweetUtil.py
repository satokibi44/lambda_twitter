from requests_oauthlib import OAuth1Session
import json

import os
import requests

from Utils.S3Util import S3Util
from Utils.SqlUtil import SqlUtil
from TweetFormetter import TweetFormetter


class TweetUtil():

    def __init__(self):
        self.CK = os.environ['CK']
        self.CS = os.environ['CS']
        self.AT = os.environ['AT']
        self.AS = os.environ['AS']
        self.session = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
        sql_util = SqlUtil()
        sql_util.create_table()
        self.user_id_list = sql_util.select_twitterid()
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

    def get_reply(self, keyword):
        url = "https://api.twitter.com/1.1/search/tweets.json"
        params = {'q': '"'+keyword+'"', 'count': 200}  # 取得数
        res = self.session.get(url, params=params)
        if res.status_code == 200:
            timelines = res.json()['statuses']
            return timelines
        else:
            print("ERROR : %d" % res.status_code)
        return

    def excute_reply(self, tweet_text, tweet_id):
        url = "https://2xa3k3mfyb.execute-api.us-east-2.amazonaws.com/dev/kusoripu-transformer-master-api"
        param = {'text': tweet_text}
        res = requests.post(url, data=json.dumps(param))
        req_body = res.json()
        reply = ""
        try:
            reply = "クソリプAI「"+req_body['decode_sentence']+"」"
        except KeyError as e:
            print(e)
            return

        print("decode_sentence:", reply)

        url = "https://api.twitter.com/1.1/statuses/update.json"
        params = {"status": reply, "in_reply_to_status_id": tweet_id,
                  "auto_populate_reply_metadata": True}

        response = self.session.post(url, params=params)
        if response.status_code == 200:
            print("Succeed!")
        else:
            print("ERROR : %d" % response.status_code)
        return

    def execute_calculate_kusoripuscore(self, tweet_text, tweet_id):
        url = "http://ecs-hands-on-1730037631.us-east-2.elb.amazonaws.com/KusorepCalculater/"
        param = {'msg': tweet_text}
        res = requests.get(url, params=param)
        req_body = res.json()
        kusoripu_score = ""
        try:
            kusoripu_score = req_body['body']['kusoripu_score']
        except KeyError as e:
            print(e)
            return

        print("kusoripu_score:", kusoripu_score)

        url = "https://api.twitter.com/1.1/statuses/update.json"
        params = {"status": "このツイートのクソリプ度は，"+str(kusoripu_score)+"点です．", "in_reply_to_status_id": tweet_id,
                  "auto_populate_reply_metadata": True}

        response = self.session.post(url, params=params)
        if response.status_code == 200:
            print("Succeed!")
        else:
            print("ERROR : %d" % response.status_code)
        return
