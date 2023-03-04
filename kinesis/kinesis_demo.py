import sys
from time import sleep
import boto3
import requests
import os

from botocore.exceptions import ClientError

url = "https://api.twitter.com/2/tweets/sample/stream"


def get_env(token_name):
    return os.environ.get(token_name)

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


# Replace with appropriate delivery stream name
aws_delivery_stream_name = 'PUT-S3-XTFxy'


def stream_connect(headers):
    kinesis_client = boto3.client('firehose',
                                  region_name=get_env("aws_region"),
                                  aws_access_key_id=get_env("aws_access_key"),
                                  aws_secret_access_key=get_env("aws_secret_access_key"))

    response = requests.request("GET", url, headers=headers, stream=True)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            _record = {'Data': response_line.decode("utf-8")}
            try:
                kinesis_client.put_record(DeliveryStreamName=aws_delivery_stream_name,
                                          Record=_record)
                p = 0
            except ClientError as e:
                print(e, file=sys.stderr)
                break
            
    
    print("Task completed")

def main():
    bearer_token = get_env("bearer_token")
    if bearer_token is not None:
        headers = create_headers(bearer_token)
        retry = 0
        while True:
            stream_connect(headers)
            wait_seconds = 2 ** retry
            sleep(wait_seconds if wait_seconds < 900 else 900)
            retry += 1
    else:
        print(
            "Error obtaining the bearer token. Please make sure you have added a valid bearer token to the config file")


if __name__ == '__main__':
    main()
