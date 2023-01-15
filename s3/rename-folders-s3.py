import boto3

client = boto3.client('s3')

# displaying my bucket names (optional)
response = client.list_buckets()
buckets = response['Buckets']
for b in buckets:
    print(f"Bucket: {b['Name']}")

bucket_name = 's3-osk-bucket-3000'
objects = client.list_objects(
    Bucket=bucket_name
)


def new_root_folder(bucket, object_list, old_dir, new_dir):
    for f in object_list['Contents']:
        if f['Size'] == 0:
            folder_name = str(f['Key'])
            folder_name = folder_name.replace(old_dir, new_dir)
            client.put_object(
                Bucket=bucket,
                Key=folder_name
            )


def move_files(bucket, object_list, old_dir, new_dir):
    for f in object_list['Contents']:
        old_file = str(f['Key'])

        if f['Size'] > 0 and old_file.__contains__(old_dir):
            file_name = old_file.replace(old_dir, new_dir)

            client.copy_object(
                Bucket=bucket,
                Key=file_name,
                CopySource={
                    'Bucket': bucket,
                    'Key': old_file
                }
            )
            print(old_file, file_name)


def recursive_folder_delete(bucket, object_list, old_dir):
    for f in object_list['Contents']:
        old_file = str(f['Key'])
        old_folder = old_dir + '/'

        if old_file.__contains__(old_folder):
            client.delete_object(
                Bucket=bucket,
                Key=old_file
            )


existing_folder = 'example'
new_folder = 'new-example'

new_root_folder(bucket_name, objects, existing_folder, new_folder)
move_files(bucket_name, objects, existing_folder, new_folder)
recursive_folder_delete(bucket_name, objects, existing_folder)
