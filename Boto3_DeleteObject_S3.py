import boto3
s3_resource=boto3.client('s3')

#delete single object
s3_resource.delete_object(Bucket="totaltechnology121874",
     Key='3 Tier.png')
     
#delete multiple objects
import os
import glob

#find all the objects from the bucket
objects=s3_resource.list_objects(Bucket="totaltechnology121874")["Contents"]
len(objects)

#iteration
for object in objects:
    s3_resource.delete_object(Bucket='totaltechnology121874',
      Key=object["Key"])