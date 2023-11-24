import boto3
ec2 = boto3.client(
    service_name='ec2',
    region_name='ap-south-1',
    aws_access_key_id='AKIAUKKU4CXXNZKXTUFP',
    aws_secret_access_key='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'
)


# ec2.create_key_pair(
#     KeyName='Derox3601',
#     KeyType='rsa')

# ec2.create_instance_event_window(
#     Name="Derox",
#     TimeRanges=[
#         {
#             'StartWeekDay': 'thursday',
#             'EndWeekDay': 'friday',
#         },
#     ],
# )

# ec2.delete_instance_event_window(
#     InstanceEventWindowId='iew-071749e00f25a58ad'
# )


