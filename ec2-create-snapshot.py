import boto3
import pprint
from datetime import datetime

ec2_client=boto3.client("ec2",region_name="us-east-2")

print("Script to create snapshots of ec2 instances on AWS")

response_instance=ec2_client.describe_instances()

if(response_instance["Reservations"]):
    for item in response_instance["Reservations"]:
        print("There are "+ str(len(item)-1) +" instances")
        for instance in item["Instances"]:
            for tag in instance["Tags"]:
                if tag["Key"]=="Name":
                    instance_name=tag["Value"]
                    #print("Instance Name:" + tag["Value"])
            print(f"Instance Name: {instance_name}")
            answer=input("Create snapshot? (yes/no): ")
            if answer.lower()=="yes":
                print("Creating snapshot")
                creation_date=datetime.now().strftime("%Y%m%d-%H-%M-%S")
                print(instance["InstanceId"])

                # response_snapshot=ec2_client.create_snapshots(
                #     Description=tag["Value"]+" snapshot "+creation_date,
                #     InstanceSpecification={
                #         "InstanceId":"i-1c0079030f4cf77d1"
                #     },
                #     TagSpecifications=[
                #         {
                #             "ResourceType":"snapshot",
                #             "Tags":[
                #                 {
                #                     "Key":"Name",
                #                     "Value":"This is a snapshot of a EC1"
                #                 },
                #             ]
                #         },
                #     ],
                #     # DryRun=True,
                # )
            else:
                print("Skip.....")
        print("")
else:
    print("There are no ec2 instances.")



#pprint.pprint(response)