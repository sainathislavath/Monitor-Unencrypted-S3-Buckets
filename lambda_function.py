import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []
    
    try:
        buckets = s3.list_buckets()['Buckets']
    except Exception as e:
        print(f"Error listing buckets: {e}")
        return
    
    for bucket in buckets:
        name = bucket['Name']
        try:
            enc = s3.get_bucket_encryption(Bucket=name)
            algo = enc['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
            print(f"[OK] {name} is encrypted with: {algo}")
        except s3.exceptions.ClientError as e:
            code = e.response['Error']['Code']
            if code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"[UNENCRYPTED] {name} has no server-side encryption!")
                unencrypted_buckets.append(name)
            else:
                print(f"[ERROR] Could not check {name}: {code}")
    
    print("🔍 Unencrypted Buckets:", unencrypted_buckets or "None")
