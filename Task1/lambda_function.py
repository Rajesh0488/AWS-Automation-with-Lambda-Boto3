import json
import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client("s3")

BUCKET_NAME = "raje-s3-bucketscleanup-demo1"

# For testing use 5 minutes
AGE_LIMIT = timedelta(minutes=5)

# Final Submission
# AGE_LIMIT = timedelta(days=30)

def lambda_handler(event, context):

    now = datetime.now(timezone.utc)

    paginator = s3.get_paginator("list_objects_v2")

    pages = paginator.paginate(Bucket=BUCKET_NAME)

    deleted = []

    for page in pages:

        if "Contents" not in page:
            continue

        for obj in page["Contents"]:

            key = obj["Key"]
            last_modified = obj["LastModified"]

            if now - last_modified > AGE_LIMIT:

                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=key
                )

                deleted.append(key)

                print(f"Deleted: {key}")

    if not deleted:
        print("No objects found for deletion.")

    return {
        "DeletedObjects": deleted
    }
