import boto3
from datetime import date

ce = boto3.client("ce")
sns = boto3.client("sns")

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:856862064332:daily-cost-alert"

THRESHOLD = 0.01

def lambda_handler(event, context):

    today = date.today()

    start = today.replace(day=1).strftime("%Y-%m-%d")
    end = today.strftime("%Y-%m-%d")

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = float(
        response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]
    )

    print(f"Current Month Cost = ${amount:.2f}")

    if amount > THRESHOLD:

        message = (
            f"AWS Monthly Cost Alert\n\n"
            f"Current Cost: ${amount:.2f}\n"
            f"Threshold: ${THRESHOLD:.2f}"
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Daily Cost Alert",
            Message=message
        )

        print("SNS Alert Sent")

    else:
        print("Threshold Not Reached")

    return {
        "statusCode": 200,
        "body": amount
    }
