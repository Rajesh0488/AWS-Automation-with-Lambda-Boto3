**Auto-Tagging EC2 Instances on Launch**

**Prerequisites**

- AWS Account
- IAM permissions to create Lambda
- Python 3.12 or higher Runtime

**Step 1: Create IAM Role for Lambda**

<img width="940" height="333" alt="image" src="https://github.com/user-attachments/assets/8e12e00f-4335-46fe-8b5e-b3e4a8c276e8" />

**Inline Policy**

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateTags",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}

**Step 2: Create Lambda Function**

<img width="940" height="342" alt="image" src="https://github.com/user-attachments/assets/fa9100bd-45f9-4a4f-820d-9cf4046ade5d" />

**Step 3: Lambda Python code**

<img width="940" height="349" alt="image" src="https://github.com/user-attachments/assets/95d05fdd-76b1-42e6-b9f3-60e7c49bfa83" />

**Step 4: Test**

<img width="940" height="379" alt="image" src="https://github.com/user-attachments/assets/105b3b73-baa6-42e5-b0fe-06e4d22eae87" />

**Step 5: Cloud Watch Logs**

<img width="940" height="349" alt="image" src="https://github.com/user-attachments/assets/f5ee1f5c-189d-44a8-add4-ef22fc73c2a1" />

**Step 6: Configuration Clean up**

<img width="940" height="384" alt="image" src="https://github.com/user-attachments/assets/031154ae-d90f-4954-930f-e65d278483fe" />

<img width="940" height="156" alt="image" src="https://github.com/user-attachments/assets/bd22dea8-1107-4ee3-b914-3d1f0a0043a6" />

<img width="940" height="207" alt="image" src="https://github.com/user-attachments/assets/c26fc64d-05cf-4020-8ece-406110567aa7" />



