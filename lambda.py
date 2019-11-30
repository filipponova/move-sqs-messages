import boto3
import os

sqs = boto3.resource('sqs')
sqs_url = os.environ['SQS_URL']
queue_dst = os.environ['QUEUE_DEST']
queue = sqs.get_queue_by_name(QueueName=queue_dst)

def lambda_handler(event,context):

    for record in event['Records']:
        ret = queue.send_message(QueueUrl=sqs_url + queue_dst, MessageBody=record['body'])
        print(ret)
