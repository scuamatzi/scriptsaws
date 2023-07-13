import boto3
import pprint

ec2_client = boto3.client("ec2", region_name="us-east-2")

response = ec2_client.describe_instances()

#pprint.pprint(response) # Print dictionary easy to read

if(response["Reservations"]):
    for item in response["Reservations"]:
        for instance in item["Instances"]:
            # Print instance Name:
            for tag in instance["Tags"]:
                if tag["Key"]=="Name":
                    print("Instance: "+tag["Value"])
            
            # Print Private IP address
            print("Private IP:" + instance["PrivateIpAddress"])

            # Print state
            state=instance["State"]["Name"]
            print("State: "+ state)

            # Print Public IP
            if(state!="stopped"):
                print("Public IP: "+ instance["PublicIpAddress"] )
            
            print("\n")
else:
    print("There are no EC2 instances.")