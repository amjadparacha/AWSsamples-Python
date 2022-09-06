import requests
import logging
import boto3
from botocore.exceptions import ClientError
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = '490473799275_Allowed_Admin_Access_N_Virginia'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

some_binary_data = 'Here we have some data'

boto3.setup_default_session(profile_name=AWS_PROFILE)

s3_client = boto3.client('s3', region_name=AWS_REGION)

def get_location():
    logger.info("in get_location()...")
    mylist = ['122.129.85.136']
    try:
        print('in try block...')
        # object = s3_resource.Object('glue-source-nbs','write/ip-location-file.txt')
        # object.put(Body=some_binary_data)

        s3_client.put_object(Body=some_binary_data, Bucket='glue-source-nbs', Key='write/ip-location-file.txt')

        logger.info("in try block....")
        for ip_address in mylist:
            api_url = "https://ipapi.co/" + ip_address + "/json"
            response = requests.get(api_url).json()
            location_data = {
                "ip": ip_address,
                "city": response.get('city'),
                "region": response.get("region"),
                "country": response.get("country_name")
            }
            return response
    except ClientError:
        logger.exception('Could not create file in S3 bucket....')
        raise
    finally:
        logger.info("process complete....")

print(get_location())
