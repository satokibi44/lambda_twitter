# coding: utf-8
import json
from Utils.TweetUtil import TweetUtil
from FindKusorepTask import FindKusorepTask
from UserRegistry import UserRegistry
from KusorepTaskExcuter import KusorepTaskExcuter
import requests
import os

def lambda_handler(event, context):
    tweet_util = TweetUtil(os.environ['AT'], os.environ['AS'])
    user_registry = UserRegistry()
    user_registry.user_manager()
    find_kusorep_task = FindKusorepTask()
    kusorep_task_excuter = KusorepTaskExcuter()
    tweet_id_list, tweet_text_list = find_kusorep_task.find_candidate_send_kusorep()
    reply_tweet_id_list, reply_text_list = find_kusorep_task.find_candidate_send_kusorepscore()
    find_kusorep_task.find_candidate_mute()
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
        kusorep_score = kusorep_task_excuter.calculate_kusorep_score(
            reply_text_list)
        for i in range(len(reply_tweet_id_list)):
            print(str(kusorep_score[i])+"点")
            if(kusorep_score[i] > 50):
                kusorep_score_message = "このリプライのクソリプ度は100点中"+str(kusorep_score[i]) + \
                    "点です．\n誹謗中傷やクソリプの可能性があります．クソリプは人を傷つける行為なので辞めましょう．\nまた，クソリプが名誉毀損として認められると3年以下の懲役若しくは禁錮又は50万円以下の罰金に処せられる可能性があります．"
                tweet_util.excute_reply(
                    kusorep_score_message, reply_tweet_id_list[i])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
