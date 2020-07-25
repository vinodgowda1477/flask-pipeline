pipeline {
  agent any
  stages {
    stage('Clone from git') {
        steps{
        git url: 'https://github.com/vinodgowda1477/flask-pipeline.git'
    }
    }
    stage('Building image and deploying container') {
      steps{
        script {
        withCredentials([string(credentialsId: 'S3_ACCESS_KEY', variable: 'S3_ACCESS_KEY'), string(credentialsId: 'S3_SECRET_ACCESS_KEY', variable: 'S3_SECRET_ACCESS_KEY'), string(credentialsId: 'S3_BUCKET_NAME', variable: 'S3_BUCKET_NAME')]) {
		sh 'sudo S3_ACCESS_KEY=$S3_ACCESS_KEY S3_SECRET_ACCESS_KEY=$S3_SECRET_ACCESS_KEY S3_BUCKET_NAME=$S3_BUCKET_NAME docker-compose up -d --build'
'
		}
        }
      }
    }
   }
  }
