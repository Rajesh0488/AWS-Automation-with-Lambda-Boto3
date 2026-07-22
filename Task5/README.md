**Restore an EC2 Instance from the Latest Snapshot**

**Prerequisites**

- AWS account is active.
- At least one EC2 instance exists.
- A snapshot of the root EBS volume already exists.
- Lambda execution role has required permissions.

**Step 1: Create IAM Role**

<img width="940" height="224" alt="image" src="https://github.com/user-attachments/assets/26978c7a-67f6-4e5a-a18e-b1c780cd9e74" />

**inline policy**

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeSnapshots",
        "ec2:RegisterImage",
        "ec2:RunInstances",
        "ec2:DescribeImages",
        "ec2:CreateTags"
      ],
      "Resource": "*"
    }
  ]
}

**Step 2: EC2 instance exists**

<img width="940" height="415" alt="image" src="https://github.com/user-attachments/assets/26825606-0a29-4649-b77e-9d7563e3f795" />

**Step 3: Snapshot Exists**

<img width="940" height="236" alt="image" src="https://github.com/user-attachments/assets/f3944d91-9b7c-4ad8-9aed-d7ae2f2fd24f" />

**Step 4: Create Lambda Function**

<img width="940" height="345" alt="image" src="https://github.com/user-attachments/assets/0905982d-d510-4404-b28d-871c842cbcee" />

**Step 5: Lambda Test**

<img width="940" height="306" alt="image" src="https://github.com/user-attachments/assets/5e640956-a778-47a7-966a-6b17286e9d41" />

<img width="940" height="235" alt="image" src="https://github.com/user-attachments/assets/92048923-828a-4900-b814-35391ffc1170" />

**Step 6: Cloud Watch Logs**

<img width="940" height="395" alt="image" src="https://github.com/user-attachments/assets/eb07ef3e-8f38-4625-81c2-003d08cf69ca" />

**Step 7: Configuration Cleanup**

<img width="940" height="225" alt="image" src="https://github.com/user-attachments/assets/86c00597-a66d-4d9f-8b95-a109031b00a3" />

<img width="940" height="237" alt="image" src="https://github.com/user-attachments/assets/7965548c-222f-4328-b56a-4004dedbdc5d" />

<img width="940" height="185" alt="image" src="https://github.com/user-attachments/assets/03eb6514-d051-42e5-a5b0-89c9ad2bcb72" />

<img width="940" height="209" alt="image" src="https://github.com/user-attachments/assets/c7cb717d-7ff0-4f93-bc12-f5fb4a1ebc24" />

<img width="940" height="122" alt="image" src="https://github.com/user-attachments/assets/5d087e23-ea3b-47b1-a837-e13ddcee8e99" />
