import boto3
from botocore.client import Config

minio_client = boto3.client('s3',
                            endpoint_url='http://192.168.1.12:9000',
                            aws_access_key_id=MINIO_ACCESS_KEY,
                            aws_secret_access_key=MINIO_SECRET,
                            config=Config(signature_version='s3v4'),
                            region_name='us-east-1')

bucket_name = 'bucket_name'

object_name = '/path/on/minio.png'
file_name = r'C:\path\to\my\file.png'

# Upload the file
try:
    minio_client.upload_file(file_name, bucket_name, object_name)
    print(f"Uploaded {file_name} to {bucket_name}/{object_name}")
except Exception as e:
    print(e)

# Get the response
try:
    response = minio_client.get_object(Bucket=bucket_name, Key=object_name)
    print(response)
except Exception as e:
    print(e)

# Delete the object
try:
    response = minio_client.delete_object(Bucket=bucket_name, Key=object_name)
    print(f"{object_name} has been deleted from {bucket_name}")
except Exception as e:
    print(e)