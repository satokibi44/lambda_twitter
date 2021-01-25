from requests_oauthlib import OAuth1Session
import urllib.request
import json

import os
import requests
import pickle

from S3Util import S3Util


class TweetUtil():

    def __init__(self):
        self.CK = os.environ['CK']
        self.CS = os.environ['CS']
        self.AT = os.environ['AT']
        self.AS = os.environ['AS']
        self.session = OAuth1Session(self.CK, self.CS, self.AT, self.AS)
        self.user_id_list = [1300452125458067457,
                             816932493962031104, 4444885817, 2799898254]

    def get_timeline(self):
        url = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=200"
        res = self.session.get(url=url)
        tweet_id_list = []
        tweet_text_list = []
        latest_tweet_id = 0
        print(latest_tweet_id)
        if res.status_code == 200:
            timelines = res.json()
            for tweet in timelines:
                if (tweet['user']['id'] in self.user_id_list):
                    s3_util = S3Util()
                    latest_tweet_id = s3_util.read_latest_tweet_id()
                    if (tweet['id'] > int(latest_tweet_id)):
                        tweet_id = tweet['id']
                        tweet_text = tweet['text']
                        tweet_id_list.append(tweet_id)
                        tweet_text_list.append(tweet_text)
                        latest_tweet_id = tweet['id']
            s3 = boto3.resource('s3')
            bucket = s3.Object(BUCKET_NAME, file_name)
            bucket.put(Body=str(latest_tweet_id))
            return tweet_id_list, tweet_text_list
        else:
            print("ERROR : %d" % res.status_code)
        return

    def excute_reply(self, tweet_text, tweet_id):
        url = "https://2xa3k3mfyb.execute-api.us-east-2.amazonaws.com/dev/kusoripu-transformer-dev-api"
        param = {'text': tweet_text}
        res = requests.post(url, data=json.dumps(param))
        req_body = res.json()
        reply = req_body['decode_sentence']

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
