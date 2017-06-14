# aws-rekognition-faces
AWS Rekognition for comparing faces 
### Process Flows
![Process](https://github.com/sjehutch/aws-rekognition-faces/blob/develop/4324214321.png?raw=true)


### 1 . You need to create a collection of face images
```
aws rekognition create-collection \
--collection-id "faces" \
--region us-east-1 \
--profile user2
```

### 2. Once step 1 is done you can get the collection name 
```
aws rekognition list-collections \
--region us-east-1 \
--profile user2 
```

### 3. Add images to the rekognition AI by sending images to it 
```
aws rekognition index-faces \
--image '{"S3Object":{"Bucket":"scottrekognition","Name":"scott.jpg"}}' \
--collection-id "faces" \
--region us-east-1 \
--profile user2
```

### 4. Test by doing something like this 
```
aws rekognition search-faces-by-image \
--image '{"S3Object":{"Bucket":"bucket-name","Name":"Example.jpg"}}' \
--collection-id "collection-id" \
--region us-east-1 \
--profile adminuser
```
```
or run python3 detect-many.py
```

### Your Response should be something like this 
```
Matched With 96.99021911621094% Similarity
To FaceId : 32276a6d-f838-558a-bc1b-6f6d6e8b79cf
Which is ImageId : 51b4f021-b8ab-5945-95ed-1c6c02db5b54
With 99.99979400634766 Confidence
```

