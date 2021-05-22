from Utils.TweetUtil import TweetUtil
from Utils.S3Util import S3Util
from TweetFormetter import TweetFormetter

class KusorepTaskExcuter():

    def find_kusorepscore_reply_candidate(self):
        tweet_id_list = []
        tweet_text_list = []
        latest_reply_id = 0
        latest_reply_id_write = 0
        s3_util = S3Util()
        tweet_util = TweetUtil()
        tweet_formetter = TweetFormetter()

        timelines = tweet_util.get_reply("クソリプ判定:")
        latest_reply_id = s3_util.read_latest_tweet_id("latest_reply_id.txt")
        for tweet in timelines:
            tweet_text = tweet_formetter.screening(tweet['text'])
            if (tweet['in_reply_to_user_id'] == self.my_twitter_id and tweet_text[:7] == "クソリプ判定:"):
                if (tweet['id'] > int(latest_reply_id)):
                    tweet_id = tweet['id']
                    tweet_id_list.append(tweet_id)
                    tweet_text_list.append(tweet_text[7:])
                    if latest_reply_id_write == 0:
                        latest_reply_id_write = tweet['id']

            s3_util.write_latest_tweet_id("latest_reply_id.txt", max(
                int(latest_reply_id_write), int(latest_reply_id)))

        return tweet_id_list, tweet_text_list
