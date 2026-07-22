import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client('ec2')

VOLUME_ID = "vol-049b129fb32209e9a"

TAG_KEY = "CreatedBy"
TAG_VALUE = "Lambda-Backup"

# test use 0 day
RETENTION_DAYS = 30 

def lambda_handler(event, context):

    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Automated Lambda Backup"
    )

    snapshot_id = snapshot['SnapshotId']

    ec2.create_tags(
        Resources=[snapshot_id],
        Tags=[
            {
                'Key': TAG_KEY,
                'Value': TAG_VALUE
            }
        ]
    )

    print(f"Created Snapshot: {snapshot_id}")

    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)

    snapshots = ec2.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': f'tag:{TAG_KEY}',
                'Values': [TAG_VALUE]
            }
        ]
    )

    deleted = []

    for snap in snapshots['Snapshots']:

        if snap['StartTime'] < cutoff:

            ec2.delete_snapshot(
                SnapshotId=snap['SnapshotId']
            )

            deleted.append(snap['SnapshotId'])

    print("Deleted Snapshots:", deleted)

    return {
        "Created": snapshot_id,
        "Deleted": deleted
    }
