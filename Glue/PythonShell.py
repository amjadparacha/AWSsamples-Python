import requests
import os
import boto3
import logging
from botocore.exceptions import ClientError

AWS_REGION = 'us-east-1'
AWS_PROFILE = '490473799275_Allowed_Admin_Access_N_Virginia'

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)

s3_client = boto3.client('s3', region_name=AWS_REGION)

endpoint = "https://ipstack.com/ipstack_api.php?ip="
token_query_string = "&token=03ANYolquR6YmYaYhpBIi72o88a0JGyMUZ8k6BkWO8V0nxoNus4E3XG8rF3pXgbyH9JMQTORIrG1GS435ts640GbePyw2GGbTGBY-ypcLizAX2pp5HosdtJHTJ55FIDKOkomc2w6wj1NiLfBi6hVO1F2EkUpw0Bxufh6u-AlOH7UIBOgBQioTCk7rcxOSWayIN4XGXrJB88W3IViFYGbTcP8qbCg-yCTVrNjiBXNB1Xv-kWFEXSqIMih39ioMb7WTFnXt5hbGo5IQYCW3G6ZiWyjHsgCbLe7J3gmwORiwmBgxVG76-DmbsfNF2f8ZWZNCpt1I9BEFkAyjmUkLn34HFU3xHJ4OUL8HV8wsRhn5GNjrlOECKi_m8K4TxpVqqItxfszzXYszlyDYA0CP9l7oCP9XhPNLfj7anjhk9a4Uc-heOGTHdZhMsG3vVkIiGs1L1rKHZg14Ms9ttHfQhU7cYkzkysNgNslMDjUtN9UmGzDWpx10ZUGW-NP_EikfVC3RXDGJSCC0it32SJ88yX2W8L85HNRlxO8yLnACEzS909nKBZZv69ithq4TUMGBbV4FmmA7fJ8nesut6"

bucket = 'glue-source-nbs'


def get_location(mylist=[]):
    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, 'ip-location-file.txt')
    writer = open(file_name, 'w')
    try:
        for ip_address in mylist:
            api_url = endpoint + ip_address + token_query_string
            response = requests.get(api_url)
            writer.writelines(response.json()['city'] + ' ' + response.json()['zip'] + ' ' + response.json()['country_name'])
            print(response.json()['city'] + ' ' + response.json()['zip'] + ' ' + response.json()['country_name'])

        logger.info('Uploading file to S3 bucket...')
        s3_client.upload_file(file_name, bucket, 'write/ip-location-file.txt')
    except ClientError:
        logger.exception('could not upload file to S3 bucket')
    finally:
        print("Traverse complete")
