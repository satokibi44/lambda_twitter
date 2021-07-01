import requests
import json

class KusorepTaskExcuter():

    def calculate_kusorep_score(self, tweet_text):
        url = "http://ecs-hands-on-1730037631.us-east-2.elb.amazonaws.com/KusorepCalculater/"
        param = {'msg': tweet_text}
        res = requests.get(url, params=param)
        req_body = res.json()
        kusoripu_score = ""
        try:
            kusoripu_score = req_body['body']['kusoripu_score']
            kusoripu_score = round(kusoripu_score*100)
        except KeyError as e:
            print(e)
            return
        return kusoripu_score

    def make_kusorep(self, tweet_text):
        url = "https://2xa3k3mfyb.execute-api.us-east-2.amazonaws.com/dev/kusoripu-transformer-master-api"
        param = {'text': tweet_text}
        res = requests.post(url, data=json.dumps(param))
        req_body = res.json()
        try:
            return "クソリプAI「"+req_body['decode_sentence']+"」"
        except KeyError as e:
            print(e)
            return

    def execute_mute(self, user_id_list, tweet_text_list, tweet_util):
        for i, v in enumerate(user_id_list):
            kusorep_score = self.calculate_kusorep_score(tweet_text_list[i])
            print(tweet_text_list[i]+" is "+str(kusorep_score))
            if(kusorep_score >= 60):
                tweet_util.excute_mute(v)