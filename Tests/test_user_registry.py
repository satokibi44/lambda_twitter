import unittest
from Utils.TweetUtil import TweetUtil
class TestUserRegistry():
    def test_add_user():
        is_tweet = False
        tweet_util = TweetUtil()
        timelines = tweet_util.get_reply("Hey!クソリプbot，クソリプを送って")
        for tweet in timelines:
            if (tweet['in_reply_to_user_id'] == tweet_util.my_twitter_id):
                is_tweet = True
        unittest.assertTrue(is_tweet)
