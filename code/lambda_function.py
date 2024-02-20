import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    sns = boto3.client('sns')
    
    security_groups = ec2.security_groups.all()
    
    for sg in security_groups:
        print(f"SG id: {sg.id} and SG name: {sg.group_name}")
        for sg_rules in sg.ip_permissions:
            for ip_range in sg_rules['IpRanges']:
                if ip_range['CidrIp'] == '0.0.0.0/0':
                    message = f"Warning!SG id: {sg.id} and SG name: {sg.group_name} allows traffic from any IP range "
                    sns.publish(TopicArn = 'Insert ARN here',
                    Message = message)
    
    
    return {
        'statusCode': 200,
        'body': 'Security audit complete'
    }
