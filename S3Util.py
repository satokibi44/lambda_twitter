import boto3


class S3Util():
    def __init__(self):
        self.BUCKET_NAME = 'kusoripu02'

    def read_latest_tweet_id(self, file_name):
        s3_client = boto3.client('s3')
        content = s3_client.get_object(Bucket=self.BUCKET_NAME, Key=file_name)
        body = content['Body'].read()  # b'テキストの中身'
        latest_tweet_id = body.decode()
        return latest_tweet_id

    def write_latest_tweet_id(self, file_name, latest_tweet_id):
        s3_resource = boto3.resource('s3')
        bucket = s3_resource.Object(self.BUCKET_NAME, file_name)
        bucket.put(Body=str(latest_tweet_id))
        return
