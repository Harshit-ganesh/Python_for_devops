import boto3

s3 = boto3.resource('s3')
bucket_name = 'harshitfirst'
file_name = "/home/harshit/Desktop/python_devops/backups/backup_2024-09-08.tar.gz"

def create_bucket(s3, bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    print("bucket created sucessfully")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name,'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded sucessfully")

create_bucket(s3,bucket_name)
# show_buckets(s3)
upload_backup(s3,file_name,bucket_name,"my_backup.tar.gz")