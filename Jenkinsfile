//Jenkinsfile

pipeline {
    agent none
    environment {
        customImage = ''
    }
    stages {
         stage('Clone repository') {
            agent any 
            steps { 
                script {
                checkout scm
                }
            }
        }

        stage('Build') { 
            agent {
                docker {
                    image 'python:3' 
                }
            }
            steps {
                script {
                    sh 'pip install wheel'
                    sh 'python3 setup.py bdist_wheel'
                    stash(name: 'lineage_app', includes: 'dist/*.whl')

                    //customImage = docker.build("lineage_flask:${env.BUILD_ID}")     
                }
            }
        }
        /*
        stage('Test'){
            steps {
                 echo 'Empty'
            }
        }
        stage('Deploy to Stage') {
            steps {
               script {
                    docker.withRegistry('https://788660851898.dkr.ecr.us-east-1.amazonaws.com/lineage_flask', 'ecr:us-east-1:ecr-user') {
                        customImage.push("${env.BUILD_NUMBER}")
                        customImage.push("stage")
                        }
                    }*/
                
    }
}
        
    