import boto3

client = boto3.client('batch')

response = client.register_job_definition(
	jobDefinitionName = 'test',
	type = 'container',
	parameters = {
		'bucket': 's3logs-manifest-qa-niaid-planx-pla-net',
		'object': 'log/manifest-qa-niaid-planx-pla-net2019-05-07-02-30-17-AE2AC923F89A6A2A' 
	},
	containerProperties = {
		'command': [
			'python2',
			'md5_stream.py',
			'-b',
			'Ref::bucket',
			'-o',
			'Ref::object'
		],
		'image': 'quay.io/cdis/awshelper:feat-aws-batch-helper',
		'jobRoleArn': 'arn:aws:iam::707767160287:role/Gen3AwsBatch',
		'memory': 500,
		'vcpus': 1,
		"environment": [
            {
                "name": "BATCH_FILE_S3_URL",
                "value": "s3://s3logs-manifest-qa-niaid-planx-pla-net/md5_stream.py"
            },
            {
                "name": "BATCH_FILE_TYPE",
                "value": "script"
            }
        ],
	},
)

print response