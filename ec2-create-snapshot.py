import boto3
import pprint

ec2_client=boto3.client("ec2",region_name="us-east-2")

response=ec2_client.create_snapshots(
    Description="Snapshot v4 of Instace EC2",
    InstanceSpecification={
        "InstanceId":"i-0c0079030f4cf77d1"
    },
    TagSpecifications=[
        {
            "ResourceType":"snapshot",
            "Tags":[
                {
                    "Key":"Name",
                    "Value":"This is a snapshot of a EC2"
                },
            ]
        },
    ],
    # DryRun=True,
)

pprint.pprint(response)