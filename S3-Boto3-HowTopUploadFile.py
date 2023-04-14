import boto3

#how to upload single file

s3_resource=boto3.client('s3')
s3_resource.upload_file(
    Filename="./Sharon-Gold-LUIT/Watermark.png",
    Bucket="totaltechnology121874",
    Key="watermarktest.png")
    

    