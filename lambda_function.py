# coding: utf-8
import json
from .Utils.TweetUtil import TweetUtil
from .Utils.SqlUtil import SqlUtil
import requests

def lambda_handler(event, context):
    tweet_util = TweetUtil()
    sql_util = SqlUtil()
    sql_util.create_table()
    tweet_id_list, tweet_text_list = tweet_util.get_timeline()
    reply_tweet_id_list, reply_text_list = tweet_util.get_reply()
    if len(tweet_id_list) != 0:
        for i in range(len(tweet_id_list)):
            tweet_util.excute_reply(tweet_text_list[i], tweet_id_list[i])
    else:
        url = "https://2xa3k3mfyb.execute-api.us-east-2.amazonaws.com/dev/kusoripu-transformer-master-api"
        param = {'text': 'test'}
        res = requests.post(url, data=json.dumps(param))

    if len(reply_tweet_id_list) != 0:
        for i in range(len(reply_tweet_id_list)):
            tweet_util.execute_calculate_kusoripuscore(
                reply_text_list[i], str(reply_tweet_id_list[i]))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
