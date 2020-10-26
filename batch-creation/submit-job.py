import boto3

client = boto3.client("batch")

response = client.submit_job(
    jobName="test-job",
    parameters={
        "bucket": "s3logs-manifest-qa-niaid-planx-pla-net",
        "object": "log/manifest-qa-niaid-planx-pla-net2019-05-13-17-57-53-1FF7CE4B81B23F12",
    },
    jobQueue="test",
    jobDefinition="test",
)
if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
    print "yo we submitted a job!!"
