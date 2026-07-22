import boto3
import os
import time

ec2 = boto3.client('ec2')

VOLUME_ID = os.environ['VOLUME_ID']
SUBNET_ID = os.environ['SUBNET_ID']
SG_ID = os.environ['SG_ID']
KEY_NAME = os.environ['KEY_NAME']

def lambda_handler(event, context):

    snapshots = ec2.describe_snapshots(
        Filters=[
            {
                'Name': 'volume-id',
                'Values': [VOLUME_ID]
            }
        ],
        OwnerIds=['self']
    )['Snapshots']

    if not snapshots:
        raise Exception("No snapshots found.")

    snapshots.sort(key=lambda x: x['StartTime'], reverse=True)

    latest_snapshot = snapshots[0]

    snapshot_id = latest_snapshot['SnapshotId']

    print(f"Latest Snapshot: {snapshot_id}")

    ami = ec2.register_image(
        Name=f"RestoreAMI-{int(time.time())}",
        RootDeviceName="/dev/xvda",
        VirtualizationType="hvm",
        Architecture="x86_64",
        EnaSupport=True,
        BlockDeviceMappings=[
            {
                "DeviceName": "/dev/xvda",
                "Ebs": {
                    "SnapshotId": snapshot_id,
                    "VolumeSize": latest_snapshot['VolumeSize'],
                    "VolumeType": "gp3",
                    "DeleteOnTermination": True
                }
            }
        ]
    )

    image_id = ami["ImageId"]

    print("AMI:", image_id)

    waiter = ec2.get_waiter('image_available')

    waiter.wait(ImageIds=[image_id])

    print("AMI Available")

    instance = ec2.run_instances(
        ImageId=image_id,
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1,
        KeyName=KEY_NAME,
        SecurityGroupIds=[SG_ID],
        SubnetId=SUBNET_ID,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'RestoredFrom',
                        'Value': snapshot_id
                    }
                ]
            }
        ]
    )

    instance_id = instance['Instances'][0]['InstanceId']

    print("New Instance:", instance_id)

    return {
        "statusCode": 200,
        "instance": instance_id,
        "snapshot": snapshot_id,
        "ami": image_id
    }
