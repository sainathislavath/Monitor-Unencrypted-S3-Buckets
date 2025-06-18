# Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

## Objective
Automatically detect any **Amazon S3 buckets that do not have server-side encryption (SSE)** enabled. This Lambda function scans all buckets in your account and logs any unencrypted buckets using Boto3.

---

## Steps Followed

### Step 1: S3 Bucket Setup
Created the following S3 buckets:

| Bucket Name                    | Encryption         |
|-------------------------------|--------------------|
| `unencrypted-bucket-sainath`  | ❌ None            |
| `encrypted-bucket-sainath`    | ✅ SSE-S3 Enabled  |

### Step 2: IAM Role Creation
- Created role: `lambda-s3-encryption-checker-role`
- Attached managed policy: `AmazonS3ReadOnlyAccess`

### Step 3: Lambda Function Setup
- Function Name: `UnencryptedS3Checker`
- Runtime: Python 3.12
- Assigned the IAM role created above
- Created a test event with `{}` payload
- Increased timeout to 30 seconds

## Screenshot
- Create 2 S3 Buckets
![Create S3 Bucket](Screenshot/3.1.png)

- Make it unencrypted
![Make it unencrypted](Screenshot/3.5.png)

- 2nd S3 Bucket
![Create Se Bucket](Screenshot/3.4.png)

- Make it encrypted
![Create S3 Bucket](Screenshot/3.2.png)

- Create IAM Role
![Create IAM Role](Screenshot/3.6.png)

- Add Permissions (AmazonS3ReadOnlyAccess)
![Add Permissions](Screenshot/3.7.png)

-Review:
![Review](Screenshot/3.8.png)

- Create Lambda Function
![Create Lambda Function](Screenshot/3.9.png)

- Test event
![Test Event](Screenshot/3.10.png)

Result:
![Result](Screenshot/3.11.png)