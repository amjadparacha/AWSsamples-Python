import boto3
import json
import logging
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-1'
AWS_PROFILE = '490473799275_Allowed_Admin_Access_N_Virginia'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)

client = boto3.client('glue', region_name=AWS_REGION)


def create_crawler():
    """
    Create Glue Crawler
    """
    try:
        response = client.create_crawler(
            Name='S3Crawler',
            Role='GlueFullAccess',
            DatabaseName='S3CrawlerNBS',
            Targets={
                'S3Targets': [
                    {
                        'Path': 's3://glue-source-nbs/read',
                        'Exclusions': [
                            'string',
                        ],
                        'SampleSize': 2
                    }
                ]
            },
            # Schedule='cron(15 12 * * ? *)',
            SchemaChangePolicy={
                'UpdateBehavior': 'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
            },
            RecrawlPolicy={
                'RecrawlBehavior': 'CRAWL_EVERYTHING'
            },
            LineageConfiguration={
                'CrawlerLineageSettings': 'DISABLE'
            }
        )
    except ClientError:
        logger.exception('Could not create glue crawler')
    else:
        logger.info(json.dumps(response, indent=4, sort_keys=True, default=str))


def start_crawler():
    try:
        response = client.list_crawlers()

        response2 = client.start_crawler(
            Name=response['CrawlerNames'][0]
        )
    except ClientError:
        logger.exception('Could not start glue crawler')
    else:
        logger.info(json.dumps(response, indent=4, sort_keys=True, default=str))

