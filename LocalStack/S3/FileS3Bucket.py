import logging
import boto3
from botocore.exceptions import ClientError
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'default'
ENDPOINT_URL = 'http://localhost:4566'

#logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)

s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)
s3_resource = boto3.resource("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)

bucket = 'hands-on-cloud-nbs-bucket'

def upload_file(file_name, bucket, object_name=None):
    """
    Upload a file to s S3 bucket.
    """
    try:
        response = s3_client.upload_file(file_name,bucket,object_name)
    except ClientError:
        logger.exception('Could not upload file to S3 bucket.')
        raise
    else:
        return response

def upload_file_main():
    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, 'test-file.txt')
    object_name = 'test-file.txt'
    logger.info('Uploading file to S3 bucket in LocalStack...')
    s3 = upload_file(file_name, bucket, object_name)
    logger.info('File uploaded to S3 bucket successfully.')


def download_file(file_name, bucket, object_name=None):
    """
    Download a file from a S3 bucket.
    """
    try:
        response = s3_resource.Bucket(bucket).download_file(object_name,file_name)
    except ClientError:
        logger.exception('Could not download file from S3 bucket')
        raise
    else:
        return response

def download_file_main():
    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, 'download-test-file.txt')
    object_name = 'test-file.txt'
    logger.info('Downloading file from S3 bucket in LocalStack...')
    s3 = download_file(file_name, bucket, object_name)
    logger.info('File downloaded from S3 bucket successfully.')


def delete_file(bucket,object_name):
    """
    Delete a file from a S3 bucket
    """
    try:
        response = s3_resource.Object(bucket, object_name).delete()
    except ClientError:
        logger.exception('Could not delete file from a S3 bucket')
        raise
    else:
        return response

def delete_file_main():
    object_name = 'test-file.txt'
    logger.info('Deleting file from S3 bucket in LocalStack...')
    s3 = delete_file(bucket,object_name)
    logger.info('File deleted from S3 bucket successfully.')
