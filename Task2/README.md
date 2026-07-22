**Automated EBS Snapshot Creation and Cleanup**

Prerequisites

- AWS Account
- Existing EC2 Instance
- Existing EBS Volume
- Python 3.12 or higher Lambda Runtime

**Step 1: Create or Identify an EBS Volume**

<img width="940" height="409" alt="image" src="https://github.com/user-attachments/assets/7dc174b4-c80e-4d12-b10a-ac20b7f51edb" />

<img width="940" height="351" alt="image" src="https://github.com/user-attachments/assets/792b371f-0ec9-48dd-b613-484720ce93ce" />

**Step 2: Create IAM Role**

<img width="940" height="436" alt="image" src="https://github.com/user-attachments/assets/e61b0e7a-d4f2-4f1a-9b12-3a40df3002fe" />

Inline Policy
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateSnapshot",
        "ec2:DescribeSnapshots",
        "ec2:DeleteSnapshot",
        "ec2:CreateTags"
      ],
      "Resource": "*"
    }
  ]
}

**Step 3: Create Lambda Function**

<img width="940" height="354" alt="image" src="https://github.com/user-attachments/assets/02228a88-cd26-4b9b-8535-412ac8a23513" />

<img width="940" height="304" alt="image" src="https://github.com/user-attachments/assets/e561baa6-1f3c-4a91-9a49-b6966f7094ad" />

**Step 4: Lambda Python Code**

<img width="940" height="218" alt="image" src="https://github.com/user-attachments/assets/5435bc69-cbd9-47ee-b6c6-a032e88cf442" />

**Step 5: Testing**

<img width="940" height="284" alt="image" src="https://github.com/user-attachments/assets/485d1d7c-be3a-4df6-b26d-9f2b15024c7d" />

<img width="940" height="373" alt="image" src="https://github.com/user-attachments/assets/36c9a47b-9760-4d68-a877-4df762e8f1d8" />

<img width="940" height="329" alt="image" src="https://github.com/user-attachments/assets/fcccfae1-6739-457f-84e9-6a773c94eab4" />

**Step 6: Cloud Watch Logs**

<img width="940" height="421" alt="image" src="https://github.com/user-attachments/assets/a919d4ad-0eed-4fda-a235-f4810069878c" />

**Step 7: Configuration Cleanup** 

<img width="940" height="242" alt="image" src="https://github.com/user-attachments/assets/a45b0acf-1e61-43e6-a449-75f69c3717d9" />

<img width="940" height="155" alt="image" src="https://github.com/user-attachments/assets/0f27f512-5612-478c-8cdd-b224a2fb2d20" />

<img width="940" height="265" alt="image" src="https://github.com/user-attachments/assets/5d6afb6f-3c89-4ff6-8b6d-333285dc23c6" />


