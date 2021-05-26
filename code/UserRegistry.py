from Utils.TweetUtil import TweetUtil
from Utils.SqlUtil import SqlUtil
from TweetFormetter import TweetFormetter
from Utils.JsonUtil import JsonUtil

class UserRegistry():
    def __init__(self) -> None:
        self.sql_util = SqlUtil()
        self.sql_util.create_latestid_table()
        self.sql_util.create_calculate_kusorep_user_table()

    def user_manager(self):
        tweet_util = TweetUtil()
        tweet_formatter = TweetFormetter()
        json_util = JsonUtil()
        timelines = tweet_util.get_reply(
            '"Hey!クソリプbot，クソリプに対して忠告して" OR "Hey!クソリプbot，クソリプに対して忠告しないで"')
        latest_registration_tweetid = self.sql_util.select_latestid(
            "latest_registration_twitterid")
        timelines = json_util.sort_reply_with_id(timelines)
        for tweet in timelines:
            if (tweet['in_reply_to_user_id'] == tweet_util.my_twitter_id):
                tweet_text = tweet_formatter.screening(tweet['text'])
                if (tweet['id'] <= int(latest_registration_tweetid)):
                    continue

                if (tweet_text == "Hey!クソリプbot，クソリプに対して忠告して"):
                    print("Hey!クソリプbot，クソリプに対して忠告して")
                    self.sql_util.insert_calculate_kusorep_user(
                        tweet['user']['screen_name'], tweet['id'])
                    latest_registration_tweetid = tweet['id']
                    reply_text = "登録しました．"
                    tweet_util.excute_reply(reply_text, tweet['id'])

                elif (tweet_text == "Hey!クソリプbot，クソリプに対して忠告しないで"):
                    print("Hey!クソリプbot，クソリプに対して忠告しないで")
                    self.sql_util.delete_calculate_kusorep_user(
                        tweet['user']['screen_name'])
                    latest_registration_tweetid = tweet['id']
                    reply_text = "登録解除しました．"
                    tweet_util.excute_reply(reply_text, tweet['id'])
        self.sql_util.insert_latestid(
            "latest_registration_twitterid", latest_registration_tweetid)

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
