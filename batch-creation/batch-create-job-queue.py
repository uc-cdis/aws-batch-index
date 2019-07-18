import boto3

client = boto3.client('batch')

response = client.create_job_queue(
	jobQueueName = 'test',
	priority = 10,
	state = 'ENABLED',
	computeEnvironmentOrder = [
		{
			'order': 1,
			'computeEnvironment': 'Luks2',
		},
	],
)

print response
