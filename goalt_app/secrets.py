import boto3

## Get RDS secret from secrets manager ##

client = boto3.client('secretsmanager')

def get_secret():
    response = client.get_secret_value(
        SecretId = 'arn:aws:secretsmanager:us-east-1:061039789243:secret:rds!db-555390f8-60f2-4d37-ad75-e63d8f0cbfa9-0s9oyX',
        region = 'us-east-1'
    )
    return response

print(get_secret())

