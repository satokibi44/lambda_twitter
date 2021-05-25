# coding: utf-8
import json
from Utils.TweetUtil import TweetUtil
from FindKusorepTask import FindKusorepTask
from UserRegistry import UserRegistry
from KusorepTaskExcuter import KusorepTaskExcuter
import requests


def lambda_handler(event, context):
    tweet_util = TweetUtil()
    user_registry = UserRegistry()
    user_registry.user_manager()
    find_kusorep_task = FindKusorepTask()
    kusorep_task_excuter = KusorepTaskExcuter()
    tweet_id_list, tweet_text_list = find_kusorep_task.find_candidate_send_kusorep()
    reply_tweet_id_list, reply_text_list = find_kusorep_task.find_candidate_send_kusorepscore()
    if len(tweet_id_list) != 0:
        for i in range(len(tweet_id_list)):
            kusorep = kusorep_task_excuter.make_kusorep(tweet_text_list[i])
            print(kusorep)
            tweet_util.excute_reply(kusorep, tweet_id_list[i])
    else:
        url = "https://2xa3k3mfyb.execute-api.us-east-2.amazonaws.com/dev/kusoripu-transformer-master-api"
        param = {'text': 'test'}
        res = requests.post(url, data=json.dumps(param))

    if len(reply_tweet_id_list) != 0:
        for i in range(len(reply_tweet_id_list)):
            kusorep_score_message = kusorep_task_excuter.make_kusorep_score(reply_text_list[i])
            tweet_util.excute_reply(kusorep_score_message, reply_tweet_id_list[i])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
