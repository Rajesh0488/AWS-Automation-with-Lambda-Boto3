# AWS-Automation-with-Lambda-Boto3

**Technologies Used**

- AWS Lambda
- Python 3.12
- Boto3
- Amazon EC2
- Amazon EBS
- Amazon S3
- Amazon SNS
- Amazon EventBridge
- AWS Cost Explorer
- IAM

 **Prerequisites**

- AWS Account
- IAM with Lambda Permission
- AWS CLI Configured
- Python 3.12 or Higher
- Boto3
- Email Address for SNS Subscription

# Modules 

1. [Automated S3 Bucket Cleanup](Task1/)
2. [Automated EBS Snapshot Creation and Cleanup](Task2/)
3. [Auto-Tagging EC2 Instances on Launch](Task3/)
4. [Daily AWS Cost Alert Using Cost Explorer API and SNS](Task4/)
5. [Restore an EC2 Instance from the Latest Snapshot](Task5/)
6. [Audit S3 Buckets for Public Access and Notify](Task6/)

# Repository Structure

AWS-Automation-with-Lambda-Boto3/
│
├── Task1-S3-Cleanup/
│      lambda_function.py
│
├── Task2-EBS-Backup/
│      lambda_function.py
│
├── Task3-EC2-AutoTag/
│      lambda_function.py
│
├── Task4-Cost-Alert/
│      lambda_function.py
│
├── Task5-EC2-Restore/
│      lambda_function.py
│
├── Task6-S3-Audit/
│      lambda_function.py
│
└── README.md
