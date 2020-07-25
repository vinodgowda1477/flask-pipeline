pipeline {
  environment {
    dockerImage = ''
  }
  agent any
  stages {
    stage('Clone from git') {
        steps{
        git url: 'https://github.com/vinodgowda1477/flask-pipeline.git'
    }
    }
    stage('Building image') {
      steps{
        script {
        withCredentials([string(credentialsId: 'S3_ACCESS_KEY', variable: 'S3_ACCESS_KEY'), string(credentialsId: 'S3_SECRET_ACCESS_KEY', variable: 'S3_SECRET_ACCESS_KEY'), string(credentialsId: 'S3_BUCKET_NAME', variable: 'S3_BUCKET_NAME')]) {
		dockerImage = docker.build("tekion_s3_upload:$BUILD_NUMBER --build-arg S3_ACCESS_KEY=$S3_ACCESS_KEY --build-arg S3_SECRET_ACCESS_KEY=$S3_SECRET_ACCESS_KEY --build-arg S3_BUCKET_NAME=$S3_BUCKET_NAME")
		}
        }
      }
    }
   }
  }
