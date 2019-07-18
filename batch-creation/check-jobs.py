import boto3

client = boto3.client('batch')

response = client.list_jobs(
    jobQueue='test',
)

print(response)