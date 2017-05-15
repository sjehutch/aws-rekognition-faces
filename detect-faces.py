# This code can go directly into a aws lambda function 

import json
import boto3

def lambda_handler(event, context):
# These below variables allow you to HTTP POST with the body as json and two keys 
    source = event['source']
    target = event['target']
    
    client = boto3.client('rekognition')
    
    response = client.compare_faces(
    SimilarityThreshold=90,
    SourceImage={
        'S3Object': {
            'Bucket': 'scottrekognition',  //Name of your S3 Bucket
            'Name': source,
        },
    },
    TargetImage={
        'S3Object': {
            'Bucket': 'scottrekognition',
            'Name': target,
        },
    },
)
    message = "The two images are a match of  {0}" .format (response['FaceMatches'][0]['Similarity'])
    return message
