from Utils.TweetUtil import TweetUtil
from Utils.SqlUtil import SqlUtil
from TweetFormetter import TweetFormetter

class UserRegistry():
    def __init__(self) -> None:
        self.sql_util = SqlUtil()
        self.sql_util.create_table()
        pass

    def user_manager(self):
        tweet_util = TweetUtil()
        tweet_formatter = TweetFormetter()
        timelines = tweet_util.get_reply(
            '"Hey!クソリプbot，クソリプを送って" and "Hey!クソリプbot，クソリプを送らないで"')
        latest_registration_tweetid = self.sql_util.select_latestid(
            "latest_registration_twitterid")
        
        for tweet in timelines:
            if (tweet['in_reply_to_user_id'] == tweet_util.my_twitter_id):
                tweet_text = tweet_formatter.screening(tweet['text'])

                if (tweet['id'] <= int(latest_registration_tweetid)):continue

                if (tweet_text == "Hey!クソリプbot，クソリプを送って"):
                    self.sql_util.insert_twitterid(tweet['user']['id'])

                elif (tweet_text == "Hey!クソリプbot，クソリプを送らないで"):
                    self.sql_util.delete_twitterid(tweet['user']['id'])

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
