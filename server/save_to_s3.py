import boto3
import uuid

session = boto3.Session(
    aws_access_key_id='ASIA2UC3EGIKEMBVEUD4',
    aws_secret_access_key='QA/lgBaQCa6TgkcoS23IPk31p4LSfbQagSRL0kiE',
    aws_session_token='IQoJb3JpZ2luX2VjENL//////////wEaCXVzLXdlc3QtMiJIMEYCIQCvZnwElX9jzMrJ6tkglEY45z8qXCXXrRIK9w2ieqH7eAIhAOR9sPjc5i42la9Yy6D6RDjiBZQFPU674YYxHAwOJJQUKrICCGsQABoMNzMwMzM1NTU2MTE2IgxO7sM973tG2A49BVYqjwI15Ek60jO0NxH6cSvRAuzeq9gKDtexZvM/4BE5ozIKc2XF8f2wDDP5lZ5Kg2mQZSEbbJ5pGz3kBfImjWOtLaYU4C3fE6xQBcdPIA1T1bT+z2WzZH5/qecvAfjhFksX/MopFZw0VZJBvXGe6E7v/TpWLGmKMQPR15TnHCy+oaqhWxu6H8eRzq4Rmzcw4lMeaT5EiBBYaa2fIMHkC7emXS/ejThu/8nF16xlp5gDoeX1ZwhwkZht0pmX1/FAqIVqhC6gsfDzSR/N9/jf/s26f6YejklQUDMspZO1cUtbMpSBcVh9bgR5ema6SIxgaG5bFLPfFbortGC0lD0N2GKcpJJqbmICwquUw6O36HPyn95nMJaeh8cGOpwBCdOoJk90c0/5wyUGn9hOj/Rmwm+6IDHFsW2xwFbevTbGm2YerCAjT9A9eDVRgpq6n+riWQAdPwS8XkM3vofy4KxONacNhOlvPZ/VWZQjzB9FtJsf1LRlKt5jQaJLFHl8TfGbd2ADwFtFmagF9hHo6w+ErTZS7+5PuCgcm9XFKnoAZD5a9aOrQNzc9aiP4mRB6zhlHiVrU2jRDP1b'
    region_name='us-east-1'
)

s3 = session.client('s3')

def add_object_to_bucket(resume):
    s3.put_object(Bucket='assignment-1-cloud-infra', Key=f"resumes/resume_{uuid.uuid1()}", Body=resume)