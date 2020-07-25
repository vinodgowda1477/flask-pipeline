import os

S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_ACCESS_KEY = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = 'https://{}.s3.amazonaws.com/'.format(S3_BUCKET_NAME)
SECRET_KEY = os.urandom(32)