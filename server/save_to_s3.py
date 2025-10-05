import boto3
import uuid

session = boto3.Session(
    aws_access_key_id='ASIA2UC3EGIKMZFDAO72',
    aws_secret_access_key='qKhXNoVxatGrksS1EMD68d9nDXN9+shA/mYAJ33I',
    aws_session_token='IQoJb3JpZ2luX2VjEM7//////////wEaCXVzLXdlc3QtMiJHMEUCIQD+Vd+RsQrW5zIWLfq0oPogx6Gl6X78bJotxZLBpTF8HwIgQJGqPR5r/8UUlIv0H9UZ1ZbRMYAMROylQvm9S7NEELwqsgIIZxAAGgw3MzAzMzU1NTYxMTYiDKWh2HLC2eE1FfspiyqPAt3TFnwAJL2zfsCulLThS1M7sOXlg5Jhw1tN/oaJjacVOZgAvviMThfTRYp3dtznaFEZWonXffH+84q4cuaYRooXXedPBDYxleoNknTNgcnMzKKVovqKIFnXAv1AhKH/S2eEMaQTOgn2EZ0R1HV38deR97A1eCIhbSZmQEfrotMB5/BniBjmGgOudYPaWQLvkG848NQMghtNZmLfvVovncei9y/4wzL7xGsu1JKToBzy7M2be/aJONkVv3UtYAF66EaJVRrfxcWql0B9rkTSi4G5HwDCK6iD5FXD1MMXzx0QmsMjnk7aXeoRMzCsda/QfSIfcQYNaLw8qJgU5/AndNwDkpih8cZ5cbTEBl38PYkwrK2GxwY6nQGVKB4eco4V3wntcQeoiz5I9oeWmB0AxTsEjZyUiSW3waav2vfqBgmdE8MqsnlaX5pPmfrgmkOgx4/t4rlFQWiPutlvlBRQWyCWHn/rZ5Yj5MJjMIguKLIs++Rq74VsPMg7wJUhP/0svxE9Or55Blb6/pEzkb/MbuFJ/bM2TY+wsavC9UA1Bepi1vHn64r8SEYUuMrlggY4maNlEv6+',
    region_name='us-east-1'
)

s3 = session.client('s3')

def add_object_to_bucket(resume):
    s3.put_object(Bucket='assignment-1-cloud-infra', Key=f"resumes/resume_{uuid.uuid1()}", Body=resume)