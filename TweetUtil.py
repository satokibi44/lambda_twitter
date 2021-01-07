from requests_oauthlib import OAuth1Session
import urllib.request
import json
import boto3
import os


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
        if res.status_code == 200:
            timelines = res.json()
            for tweet in timelines:
                if (tweet['user']['id'] in self.user_id_list):
                    tweet_id = tweet['id']
                    tweet_text = tweet['text']
                    tweet_id_list.append(tweet_id)
                    tweet_text_list.append(tweet_text)
            return tweet_id_list, tweet_text_list
        else:
            print("ERROR : %d" % res.status_code)
        return

    def excute_reply(self, tweet_text, tweet_id):
        input_event = {
        "text": tweet_text
        }
        Payload = json.dumps(input_event)
        res = boto3.client('lambda').invoke(
            FunctionName='kusoripu-transformer-dev-api',
            InvocationType='RequestResponse', # Event or RequestResponse
            Payload=Payload
            )
        payload = res['Payload'].read().decode('utf-8')
        
        json_load = json.loads(payload)
        reply = json_load['body']
        json_load = json.loads(reply)
        reply = json_load['decode_sentence']
        
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
