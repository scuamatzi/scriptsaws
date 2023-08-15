import boto3
import pprint
from datetime import datetime

ec2_client=boto3.client("ec2",region_name="us-east-2")

print("Script to create snapshots of ec2 instances on AWS\n")

response_instance=ec2_client.describe_instances()

if(response_instance["Reservations"]):
    print("There are "+ str(len(response_instance["Reservations"])) +" instances")
    for item in response_instance["Reservations"]:
        for instance in item["Instances"]:
            for tag in instance["Tags"]:
                if tag["Key"]=="Name":
                    instance_name=tag["Value"]
            print(f"Instance Name: {instance_name}")
            answer=input("Create snapshot? (yes/no): ")
            if answer.lower()=="yes":
                print("Creating snapshot")
                creation_date=datetime.now().strftime("%Y%m%d-%H-%M-%S")

                response_snapshot=ec2_client.create_snapshots(
                    Description=instance_name +" snapshot on " +creation_date,
                    InstanceSpecification={
                        "InstanceId":instance["InstanceId"]
                    },
                    TagSpecifications=[
                        {
                            "ResourceType":"snapshot",
                            "Tags":[
                                {
                                    "Key":"Name",
                                    "Value":instance_name+" snapshot on "+creation_date
                                },
                            ]
                        },
                    ],
                )
                print("Snapshot ID: "+response_snapshot["Snapshots"][0]["SnapshotId"])
                print("....Done\n")
            else:
                print("Skip.....\n")
else:
    print("There are no ec2 instances.")


