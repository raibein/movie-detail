pipeline {
  
  agent any
  
  environment {
    dockerHubUrl = 'rabenshrestha'
    backendRegistry = 'rabenshrestha/movie-backend:latest'
    frontendRegistry = 'rabenshrestha/movie-frontend:latest'
  }

  stages {
    stage ('Fetch from Git') {
      steps {
        git branch: 'automate', credentialsId: 'gitAuth', url: 'https://github.com/raibein/movie-detail.git'
      }
    }
    stage ('Backend Docker Build and Push') {
      steps {
        // build
        sh 'docker build -t rabenshrestha/movie-backend:latest ./backend/'
        
        sh 'echo Backend Docker Image Push to Docker Register'
        withDockerRegistry(credentialsId: 'dockerAuth', url: dockerHubUrl) {
            // some block
            sh 'docker image push ' . backendRegistry
        }
      }
    }
    stage ('Frontend Docker Build and Push') {
      steps {
        // build
        sh 'docker build -t rabenshrestha/movie-frontend:latest ./frontend/'
      }
      sh 'echo Frontend Docker Image Push to Docker Register'
        withDockerRegistry(credentialsId: 'dockerAuth', url: dockerHubUrl) {
            // some block
            sh 'docker image push ' . frontendRegistry
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}