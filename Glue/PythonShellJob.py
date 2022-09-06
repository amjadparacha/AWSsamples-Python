import boto3
import json

client = boto3.client('glue', region_name="us-east-1")

response = client.create_job(
    Name='PythonShellJob',
    Role='GlueFullAccess'
)
