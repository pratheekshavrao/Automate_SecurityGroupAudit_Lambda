
# Automate Security Group Audit process with Lambda 

This project creates an Audit System designed to scrutinize Security Groups for potential security vulnerabilities, specifically focusing on inbound rules permitting traffic from any IP address (0.0.0.0/0). To implement this, a Lambda function will be created to systematically monitor all security groups within the account, examining their inbound rules. If any security group is identified with such permissive rules, the system will generate a comprehensive report and dispatch it via email using the Simple Notification Service (SNS).

## Prerequisites

Make sure there are some Security groups in your account and also some with inbound rules which allow traffic from 0.0.0.0/0 for testing purposes.

## Steps to execute

1.	Create an SNS (Simple Notification Service) topic with a meaningful name. Subsequently, set up a subscriber for the topic using an email address. Ensure confirmation of the email subscription to complete the setup.

2.	Next to create a Lambda function,  navigate to Lambda console. Click on "Create function". Choose a meaningful name for your Lambda function, specify the runtime as Python 3.9, and create a new role.

3. For local testing of Lambda functions, download the functions to Cloud9 environment, create event.json and template .yaml files. Use below code from terminal to test the functions.sam local invoke YourLambdaFunctionName -e event.json 

4. Upon successful local testing, upload the Lambda function code from Cloud9 to AWS Lambda.

5.	Grant Permissions to Lambda for EC2 Access and SNS.Attach an IAM policy to the Lambda Execution Role to permit access to EC2 resources to access Security Groups and also for SNS. 

6.	To configure Amazon EventBridge Scheduler navigate to the Amazon EventBridge console.  Create a new schedule with a schedule expression, specifying a recurrence pattern for weekly execution at a designated time. Set the scheduler’s target to be your Lambda function.

## Result

An email is received with the details of Security Groups with inbound rules set as 0.0.0.0/0
