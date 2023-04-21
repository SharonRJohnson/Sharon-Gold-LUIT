# Creating a SQS using python

import boto3
client = boto3.client("sqs")

# Create a SQS queue
queue = client.create_queue(
    QueueName="LUIT_Week15_Project")
    
# Retrieving url
url = client.get_queue_url(
    QueueName="LUIT_Week15_Project",
    )
print(url["QueueUrl"])    