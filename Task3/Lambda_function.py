import boto3
from datetime import datetime, timezone

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print("Received Event:", event)

    try:
        instance_id = event["detail"]["instance-id"]
    except KeyError:
        print("Error: event has no detail.instance-id — check the EventBridge rule pattern")
        return {"statusCode": 400, "body": "Missing instance-id in event"}

    launch_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {"Key": "LaunchDate", "Value": launch_date},
                {"Key": "Environment", "Value": "Development"}
            ]
        )
    except Exception as e:
        print(f"Failed to tag instance {instance_id}: {e}")
        return {"statusCode": 500, "body": f"Failed to tag {instance_id}"}

    print(f"Successfully tagged instance {instance_id}")
    return {
        "statusCode": 200,
        "body": f"Tagged {instance_id}"
    }
