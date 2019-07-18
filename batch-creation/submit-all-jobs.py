import boto3

s3 = boto3.resource('s3')
conn = boto3.client('s3')
client = boto3.client('batch')

bucketName = 's3logs-manifest-qa-niaid-planx-pla-net'

jobIndex = 0
for obj in conn.list_objects(Bucket = bucketName)['Contents']:
	key = str(obj['Key'])
	print "submitting job for " + key
	job = 'test-' + str(jobIndex) 
	jobIndex = jobIndex + 1
	response = client.submit_job(
		jobName = job,
		parameters = {
			'bucket': bucketName,
			'object': obj['Key']
		},
		jobQueue = 'test',
		jobDefinition = 'test',
	)
	if response['ResponseMetadata']['HTTPStatusCode'] != 200:
		print 'there was a problem with submitting the job for ' + key