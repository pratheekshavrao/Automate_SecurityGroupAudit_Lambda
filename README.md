
# Automate Security Group Audit process with Lambda 

This project creates an Audit System designed to scrutinize Security Groups for potential security vulnerabilities, specifically focusing on inbound rules permitting traffic from any IP address (0.0.0.0/0). To implement this, a Lambda function will be created to systematically monitor all security groups within the account, examining their inbound rules. If any security group is identified with such permissive rules, the system will generate a comprehensive report and dispatch it via email using the Simple Notification Service (SNS).

