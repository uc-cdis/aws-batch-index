import boto3

client = boto3.client("batch")

response = client.update_compute_environment(
    type="MANAGED",
    computeEnvironmentName="M4Spot",
    computeResources={
        "type": "SPOT",
        "bidPercentage": 20,
        "desiredvCpus": 4,
        "ec2KeyPair": "id_rsa",
        "instanceRole": "ecsInstanceRole",
        "instanceTypes": [
            "m4",
        ],
        "maxvCpus": 128,
        "minvCpus": 0,
        "securityGroupIds": [
            "sg-cf5093b2",
        ],
        "spotIamFleetRole": "arn:aws:iam::707767160287:role/aws-ec2-spot-fleet-role",
        "subnets": [
            "subnet-220c0e0a",
            "subnet-1a95556d",
            "subnet-978f6dce",
        ],
        "tags": {
            "Name": "Batch Instance - M4Spot",
        },
    },
    serviceRole="arn:aws:iam::707767160287:role/AWSBatchServiceRole",
    state="ENABLED",
)

print response
