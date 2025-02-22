import boto3, json

## Get RDS secret from secrets manager ##

client = boto3.client('secretsmanager', region_name='us-east-1')

def get_secret():
    response = client.get_secret_value(
        SecretId = 'arn:aws:secretsmanager:us-east-1:061039789243:secret:rds!db-555390f8-60f2-4d37-ad75-e63d8f0cbfa9-0s9oyX'
    )

    try:
        secret_response = client.get_secret_value(SecretId='arn:aws:secretsmanager:us-east-1:061039789243:secret:rds!db-555390f8-60f2-4d37-ad75-e63d8f0cbfa9-0s9oyX')
        secret = secret_response['SecretString']
        json_secret = json.loads(secret)
        credentials = {
            'username': json_secret['username'],
            'password': json_secret['password']
        }
        return credentials
    except ClientError as e:
        raise e
    
print(get_secret())