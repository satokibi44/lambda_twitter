from Utils.TweetUtil import TweetUtil
from TweetFormetter import TweetFormetter
from Utils.SqlUtil import SqlUtil
from Utils.JsonUtil import JsonUtil

class FindKusorepTask():

    def __init__(self):
        sql_util = SqlUtil()
        sql_util.create_table()
        self.user_id_list = sql_util.select_twitterid()

    def find_candidate_regist_userlist():
        pass

    def find_candidate_delete_userlist():
        pass

    def find_candidate_send_kusorepscore(self):
        tweet_id_list = []
        tweet_text_list = []
        latest_reply_id = 0
        tweet_util = TweetUtil()
        tweet_formetter = TweetFormetter()
        json_util = JsonUtil()

        timelines = tweet_util.get_reply('"クソリプ判定:"')
        timelines = json_util.sort_reply_with_id(timelines)
        latest_reply_id = self.sql_util.select_latestid(
            "latest_reply_id")
        for tweet in timelines:
            tweet_text = tweet_formetter.screening(tweet['text'])
            if (tweet['id'] <= int(latest_reply_id)):continue

            if (tweet['in_reply_to_user_id'] == tweet_util.my_twitter_id and tweet_text[:7] == "クソリプ判定:"):
                tweet_id = tweet['id']
                tweet_id_list.append(tweet_id)
                tweet_text_list.append(tweet_text[7:])
                latest_reply_id = tweet['id']

        self.sql_util.insert_latestid(
            "latest_registration_twitterid", latest_reply_id)

        return tweet_id_list, tweet_text_list

    def find_candidate_send_kusorep(self):
        tweet_id_list = []
        tweet_text_list = []
        latest_tweet_id = 0
        tweet_util = TweetUtil()
        tweet_formetter = TweetFormetter()
        json_util = JsonUtil()

        timelines = tweet_util.get_timeline()
        timelines = json_util.sort_reply_with_id(timelines)
        latest_tweet_id = self.sql_util.select_latestid("latest_tweet_id")
        for tweet in timelines:
            if (tweet['id'] <= int(latest_tweet_id)):continue
            if (tweet['user']['id'] in self.user_id_list):
                tweet_id = tweet['id']
                tweet_text = tweet_formetter.screening(tweet['text'])
                tweet_id_list.append(tweet_id)
                tweet_text_list.append(tweet_text)
                latest_tweet_id = tweet['id']
        self.sql_util.insert_latestid("latest_tweet_id", latest_tweet_id)

        return tweet_id_list, tweet_text_list
