# Account creation and setup procedure
These are the steps I took when creating and setting up the account. Maybe it will be split in more docs later on.  
Everithing is based on the youtube video [Getting Started With AWS Cloud | Step-by-Step Guide](https://www.youtube.com/watch?v=CjKhQoYeR4Q&ab_channel=TravisMedia)

## Account creation
1. Go to [AWS Management Console](https://aws.amazon.com/console/)
2. Click on "Create an AWS Account"
3. Fill in the required information (Root user email address, and AWS account name)
4. Enter verification code from the mail
5. Setup the root password
6. Enter contact information
7. Enter billing information
8. Confirm the identity with a phone number
9. Choose a support plan
10. Sign in using the root user

## Setting up IAM
1. Go to the [IAM console](https://console.aws.amazon.com/iam/)
2. Add MFA for the root user
3. Create a new user
4. Select the "Provide access to AWS Management Console" option
5. Create a password and select the "Require password reset" option
6. Add the user to a group or add policies directly (we go for policy for simplicity)
7. Attach the "AdministratorAccess" policy
8. Copy the sign-in link and add it as a bookmark

## Create a billing alarm
1. Go to the [Setting up your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#billing-access) and make sure you have completed the "Grant access to the billing console" steps 
2. Go to the [Create a billing alarm guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) and follow the instructions

## Set up the CLI
1. Go to the [AWS Command Line Interface page](https://aws.amazon.com/cli/) and click on [Get started](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and find the [installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) for your OS
2. Install the CLI (For Windows ```msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi```
3. Check if the installation is successful by running ```aws --version```. Remember to restart the terminal if you had it open during the installation
4. Go to the user you created in the IAM console and click on the "Security credentials" tab and create an access key for CLI
5. I downloaded the key file and saved it and also added the file to the .gitignore file. No need to download, I just don't want to create new ones
6. Run ```aws configure``` and enter the access key and secret key. The other two parameters are optional

## Test EC2 instance
1. Go to the [EC2 console](https://console.aws.amazon.com/ec2/)
2. Click on "Launch instance", select an Amazon Machine Image (AMI) and choose an instance type. Always look for free tier instances to keep it free.
3. Create a new key pair and download the key pair file. I added mine in the repo and added entry in .gitignore to not upload it
4. Create new security group or select an existing one (new works before we set up anything) and allow SSH from anywhere
5. Launch the instance. It should be available in the list. Select it and go to actions/connect to get the connection instructions
    - You can use the EC2 Instance Connect (browser-based SSH connection) or use the SSH client.
    - The SSH comand should look like this ```ssh -i "your_key.pem" ec2-user@ec2-instance-id.eu-north-1.compute.amazonaws.com"```
6. Terminate by selecting the instance from the list and clicking on "Instance state/Terminate (delete) instances"