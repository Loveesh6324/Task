import boto3
import pandas as pd


s3 = boto3.client('s3')

s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIAULICBHAMZPW5FXKN',
    aws_secret_access_key='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'
)
# Print Buckets Name
# for bucket in s3.buckets.all():
#     print(bucket.name)

# foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
# bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})

# foo.to_csv('foo.csv')
# bar.to_csv('bar.csv')

# Upload File To Bucket
# s3.Bucket('loveesh3601').upload_file(Filename='foo.csv', Key='foo.csv')
# s3.Bucket('loveesh3601').upload_file(Filename='bar.csv', Key='bar.csv')


# for obj in s3.Bucket('dd12341231212').objects.all():
#     print(obj)


# Delete File From Bucket
# s3.Object('dd12341231212', 'foo.csv').delete()
# s3.Object('dd12341231212', 'bar.csv').delete()


bucket = s3.Bucket('loveesh3601')
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
    
print(body)