class S3Util():
    import boto3
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.BUCKET_NAME = 'kusoripu02'

    def read_latest_tweet_id(self):
        file_name = 'latest_tweet_id.txt'
        content = self.s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
        body = content['Body'].read()  # b'テキストの中身'
        latest_tweet_id = body.decode()
        return latest_tweet_id
