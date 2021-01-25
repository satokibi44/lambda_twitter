# coding: utf-8
import json
from TweetUtil import TweetUtil

def lambda_handler(event, context):
    tweetUtil = TweetUtil()
    tweet_id_list, tweet_text_list = tweetUtil.get_timeline()
    reply_tweet_id_list, reply_text_list = tweetUtil.get_reply()
    if len(tweet_id_list) != 0:
        for i in range(len(tweet_id_list)):
            tweetUtil.excute_reply(tweet_text_list[i], tweet_id_list[i])
    if len(reply_tweet_id_list) != 0:
        for i in range(len(reply_tweet_id_list)):
            tweetUtil.execute_calculate_kusoripuscore(reply_text_list[i], str(reply_tweet_id_list[i]))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }