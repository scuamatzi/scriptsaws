# Scripts  for AWS

### ec2-create.py

This script just create an EC2 instance.

`region_name="us-east-2"` needs to be adjusted

`number_of_servers=2` changed to the number of servers to be created

`"AvailabilityZone":"us-east-2a"`  should be adjusted

`"Value":f"testsrv{item}"` -> word `testsrv` should be adjusted. `item` is a counter starting from 1

It prints:

`Instance Name`

`Instance ID`

`Private IP`

`Public IP`

### ec2-list.py

This script list all EC2 instances on AWS.

`region_name="us-east-2"` needs to be adjusted

It prints:

`Instance Name`

`Instance ID`

`Private IP`

`State`

`Public IP` -> only if the instance is running

### ec2-create-snapshot.py

This script creates snapshots of EC2 instances. It ask one by one.

`region_name="us-east-2"` needs to be adjusted

It prints:

`Snapshot ID`
