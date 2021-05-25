from Utils.TweetUtil import TweetUtil
from Utils.SqlUtil import SqlUtil

class UserRegistry():
    def __init__(self) -> None:
        self.sql_util = SqlUtil()
        self.sql_util.create_table("User")

    def add_user(self):
        tweet_util = TweetUtil()
        timelines = tweet_util.get_reply("Hey!クソリプbot，クソリプを送って")
        for tweet in timelines:
            if (tweet['in_reply_to_user_id'] == tweet_util.my_twitter_id):
                self.sql_util.insert_twitterid(tweet['user']['id'])

    def remove_user(self):
        tweet_util = TweetUtil()
        timelines = tweet_util.get_reply("Hey!クソリプbot，クソリプを送らないで")
        for tweet in timelines:
            if (tweet['in_reply_to_user_id'] == tweet_util.my_twitter_id):
                self.sql_util.delete_twitterid(tweet['user']['id'])
