import boto3

# AWS credentials for you're profile
access_key = "your keys" 
secret_key = "your keys"
region = "your region"

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

# Connect to DynamoDB
dynamodb = session.resource('dynamodb')

# create the table
table = dynamodb.create_table(
    TableName='FavoriteIceCream', 
    KeySchema=[
        {
            'AttributeName': 'brand', 
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'flavor', 
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'brand', 
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'flavor', 
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


# print message
print("Table Created!")


    












