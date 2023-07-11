import boto3
import pprint

ec2_client = boto3.client("ec2", region_name="us-east-2")

#response = client.describe_instances()
response = ec2_client.describe_instances()

#print(response)
pprint.pprint(response)

for item in response["Reservations"]:
    print(len(item["Instances"]))