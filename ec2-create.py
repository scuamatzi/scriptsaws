import boto3
import pprint

ec2_client= boto3.client("ec2",region_name="us-east-2")
#other parameters for client:
#aws_access_key_id
#aws_secret_access_key

response = ec2_client.run_instances(
    ImageId="ami-024e6efaf93d85776",
    InstanceType="t2.micro",
    KeyName="testkey",
    MaxCount=1,
    MinCount=1,
    Placement={
        "AvailabilityZone":"us-east-2a"
    },
    SecurityGroupIds=["sg-061efb035d2d3124d"],
    SubnetId="subnet-007b29710ad02f48b",
    TagSpecifications=[
        {
            "ResourceType":"instance",
            "Tags":[
                {
                    "Key":"Name",
                    "Value":"deploysrv2"
                },
            ]
        },
    ]
)

f=open("newservers.txt", "a")
f.write(str(response)+"\n\n")
f.close

#pprint.pprint(response)