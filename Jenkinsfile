//Jenkinsfile

pipeline {
    agent any
    
    stages {
         stage('Clone repository') { 
            steps { 
                script {
                checkout scm
                }
            }
        }

        stage('Build') { 
            steps {
                script {
                    def customImage = docker.build("lineage_flask:${env.BUILD_ID}")     
        }
        }
        }
        stage('Test'){
            steps {
                 echo 'Empty'
            }
        }
        stage('Deploy') {
            steps {
               script {
                    docker.withRegistry('https://788660851898.dkr.ecr.us-east-1.amazonaws.com/lineage_flask', 'ecr:us-east-1:ecr-user') {
                        customImage.push("${env.BUILD_NUMBER}")
                        customImage.push("latest")
                        }
                    }
                
                }
            }
        }
    }