import boto3
import pprint

ec2_client= boto3.client("ec2",region_name="us-east-2")
#other parameters for client:
#aws_access_key_id
#aws_secret_access_key

number_of_servers=2
item=1

while item<=number_of_servers:

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
                        "Value":f"deploysrv{item}"
                    },
                ]
            },
        ]
    )

    instance_id=response["Instances"][0]["InstanceId"]

    # Wait for instance to be running
    ec2_client.get_waiter("instance_running").wait(InstanceIds=[instance_id])

    # Print Instance Name
    print("Server: "+ response["Instances"][0]["Tags"][0]["Value"])

    # Print Instance ID
    #print(response["Instances"][0]["InstanceId"])
    print("Instance ID: "+ instance_id)

    # Print Private IP
    print("Private IP: "+ response["Instances"][0]["PrivateIpAddress"])

    # Print Public ID
    public_ip=ec2_client.describe_instances(InstanceIds=[instance_id])["Reservations"][0]["Instances"][0]["PublicIpAddress"]

    print("Public IP: "+ public_ip)

    f=open("newservers.txt", "a")
    f.write(str(response)+"\n\n")
    f.close
    item+=1

#pprint.pprint(response)