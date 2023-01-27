import boto3

# Create an IAM client
iam = boto3.client('iam')

# List all users in the IAM console
response = iam.list_users()
users = response['Users']

# Print the user names
for user in users:
    print(user['UserName'])