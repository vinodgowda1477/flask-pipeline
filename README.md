##Introduction:
This is a flask based web application with login to upload files to s3 and list the files uploaded in the destination bucket.

##Prerequisites:
- aws user(programmatic access) with read write permission to aws s3 service.  
- Pre-installed Ansible, Docker, docker-compose, Jenkins.

##Provisioning - if required

Provisional scripts are used for
 - Install Python3 along with its package boto3 required for aws s3 bucket creation.
 - Created bucket with desired name on aws    
 - Provision host with new-relic to monitor the performance.
 
 How to run?
 Step 1: Replace all the variables in the file provsion/group_vars/local as per requirements
 Step 2: change the directory to base folder of the project and run ./setup.sh to provision the local machine.
 
 
 ## Pipeline for building and deploying flask app.
 
 How to create pipeline:
 Step 1: On jenkins dashboard create a global credentials of kind secret test with ID S3_ACCESS_KEY,S3_SECRET_ACCESS_KEY and S3_BUCKET_NAME which will be used by Jenkinsfile later.
  
  S3_ACCESS_KEY - same aws access key used to create bucket using ansible
  S3_SECRET_ACCESS_KEY - same aws secret key used to create bucket using ansible 
  S3_BUCKET_NAME - name of the desired bucket where files needs to be stored.
  
 Step 2: Create a pipeline which reads the Jenkins file from the repo - https://github.com/vinodgowda1477/flask-pipeline.git
 
 Step 3: Click on build now to build application and deploy on container.
 
 
 ####Once deployed application can be accessed using following creds
  
  url: http://locahost:8000
  username: admin
  password: admin