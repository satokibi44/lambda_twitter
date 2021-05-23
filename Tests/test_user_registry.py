import unittest
from Utils.TweetUtil import TweetUtil
class TestUserRegistry():
    def test_add_user():
        user_id = 0
        tweet_util = TweetUtil()
        timelines = tweet_util.get_reply("Hey!クソリプbot，クソリプを送って")
        for tweet in timelines:
            if (tweet['in_reply_to_user_id'] == tweet_util.my_twitter_id):
                user_id = tweet['user']['id']
        unittest.assertEqual(1353572204915507200, user_id)
