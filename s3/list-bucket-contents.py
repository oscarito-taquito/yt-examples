import boto3
client = boto3.client('s3')

buckets = client.list_buckets()

for b in buckets['Buckets']:
    objects = client.list_objects(
        Bucket=b['Name']
    )

    for o in objects['Contents']:
        if o['Size'] > 0:
            print(f"Bucket: {b['Name']} Filepath: {o['Key']}")



