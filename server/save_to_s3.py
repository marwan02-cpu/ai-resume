import boto3
import uuid

session = boto3.Session(
    aws_access_key_id='AWS_ACCESS_KEY_ID',
    aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
    aws_session_token='AWS_SESSION_TOKEN',
    region_name='REGION_NAME'
)

s3 = session.client('s3')

def add_object_to_bucket(resume):
    s3.put_object(Bucket='BUCKET_NAME', Key=f"FILE_NAME", Body=resume)