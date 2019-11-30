conf = {
  "aws-access-key": "",
  "aws-secret-key": "",
  "sqs-queue-src": "",
  "sqs-queue-dst": "",
}

import boto3
client = boto3.client(
    'sqs',
        aws_access_key_id       = conf.get('aws-access-key'),
        aws_secret_access_key   = conf.get('aws-secret-key')
)

while True:
    messages = client.receive_message(QueueUrl=conf['sqs-queue-src'], MaxNumberOfMessages=10, WaitTimeSeconds=0)

    if 'Messages' in messages:
        for m in messages['Messages']:
            print(m['Body'])
            ret = client.send_message(QueueUrl=conf['sqs-queue-dst'], MessageBody=m['Body'])
            print(ret)
            client.delete_message(QueueUrl=conf['sqs-queue-src'], ReceiptHandle=m['ReceiptHandle'])
    else:
        print('Queue is currently empty or messages are invisible')
        break
