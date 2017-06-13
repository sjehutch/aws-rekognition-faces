import boto3

BUCKET = "face-source-scott"  ### This is the bucket where the face your trying to match lives
KEY = "rishi4.jpg"   ## This is the face your are trying to match 
COLLECTION = "faces" #### This is the collection of faces that you have already taught the ai to store

def search_faces_by_image(bucket, key, collection_id, threshold=80, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.search_faces_by_image(
        Image={
            "S3Object": {
                "Bucket": bucket,
				"Name": key,
            }
        },
        CollectionId=collection_id,
        FaceMatchThreshold=threshold,
    )
    return response['FaceMatches']

for record in search_faces_by_image(BUCKET, KEY, COLLECTION):
    face = record['Face']
   
    print ("Matched With {}""%"" Similarity".format(record['Similarity']))
    print ("To FaceId : {}".format(face['FaceId']))
    print ("Which is ImageId : {}".format(face['ImageId']))
    print ("With {} Confidence".format(face['Confidence']))
    


