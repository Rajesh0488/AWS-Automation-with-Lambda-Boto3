import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:us-east-1:856862064332:S3PublicBucketAlert"

def lambda_handler(event, context):

    buckets = s3.list_buckets()["Buckets"]

    findings = []

    for bucket in buckets:

        bucket_name = bucket["Name"]

        public_reasons = []

        # ----------------------------
        # Check Block Public Access
        # ----------------------------
        try:
            response = s3.get_public_access_block(
                Bucket=bucket_name
            )

            config = response["PublicAccessBlockConfiguration"]

            if not all(config.values()):
                public_reasons.append(
                    "Block Public Access is NOT fully enabled"
                )

        except ClientError as e:

            code = e.response["Error"]["Code"]

            if code == "NoSuchPublicAccessBlockConfiguration":
                public_reasons.append(
                    "No Public Access Block Configuration"
                )
            else:
                public_reasons.append(
                    f"Unable to check Public Access Block ({code})"
                )

        # ----------------------------
        # Bucket Policy Status
        # ----------------------------
        try:

            policy = s3.get_bucket_policy_status(
                Bucket=bucket_name
            )

            if policy["PolicyStatus"]["IsPublic"]:
                public_reasons.append(
                    "Bucket Policy is PUBLIC"
                )

        except ClientError:
            pass

        # ----------------------------
        # Bucket ACL
        # ----------------------------
        try:

            acl = s3.get_bucket_acl(
                Bucket=bucket_name
            )

            for grant in acl["Grants"]:

                grantee = grant["Grantee"]

                uri = grantee.get("URI", "")

                if "AllUsers" in uri or "AuthenticatedUsers" in uri:
                    public_reasons.append(
                        "ACL allows public access"
                    )

        except ClientError:
            pass

        if public_reasons:

            findings.append(
                f"Bucket: {bucket_name}\n"
                + "\n".join(public_reasons)
            )

    if findings:

        message = (
            "WARNING!\n\n"
            "The following S3 bucket(s) may be publicly accessible:\n\n"
            + "\n\n".join(findings)
        )

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="S3 Public Bucket Alert",
            Message=message
        )

        print(message)

    else:

        print("No public buckets found.")

    return {
        "statusCode":200,
        "body":"Audit completed"
    }
