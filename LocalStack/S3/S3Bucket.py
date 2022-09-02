import logging
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'default'
ENDPOINT_URL = 'http://localhost:4566'

#logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)

s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)

bucket_name = 'hands-on-cloud-nbs-bucket'

def create_bucket(bucket_name):
    """
    Create a S3 bucket
    """
    try:
        response = s3_client.create_bucket(Bucket=bucket_name)
    except ClientError:
        logger.exception('Could not create S3 bucket locally.')
    else:
        return response

def create_bucket_main():
    """
    Main invocation function.
    """

    logger.info('Creating S3 bucket locally using LocalStack...')
    s3 = create_bucket(bucket_name)
    logger.info('S3 bucket created.')
    logger.info(json.dumps(s3, indent=4) + '\n')

def delete_bucket(bucket_name):
    """
    Delete a S3 bucket
    """
    try:
        response = s3_client.delete_bucket(Bucket=bucket_name)
    except ClientError:
        logger.exception('Could not delete S3 bucket locally.')
        raise
    else:
        return response

def delete_bucket_main():
    logger.info('Deleting S3 bucket...')
    s3 = delete_bucket(bucket_name)
    logger.info('S3 bucket deleted.')
    logger.info(json.dumps(s3, indent=4) + '\n')
