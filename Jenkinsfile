pipeline {
  
  agent any
  
  environment {
    dockerHubUrl = 'rabenshrestha'
    backendRegistry = 'rabenshrestha/movie-backend:latest'
    frontendRegistry = 'rabenshrestha/movie-frontend:latest'
    DOCKERHUB_CREDENTIALS = credentials('dockerAuth')
  }

  stages {
    stage ('Fetch from Git') {
      steps {
        git branch: 'automate', credentialsId: 'gitAuth', url: 'https://github.com/raibein/movie-detail.git'
      }
    }
    stage ('Backend Docker Build') {
      steps {
        // build
        sh 'docker build -t rabenshrestha/movie-backend:latest ./backend/'
      }
    }
    // stage ('Frontend Docker Build') {
    //   steps {
    //     // build
    //     sh 'docker build -t rabenshrestha/movie-frontend:latest ./frontend/'
    //   }
    // }
    stage ('Docker Login') {
      steps {
        // Login
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage ('Backend Docker Push') {
      steps {
        // Backend Docker Push
        sh 'docker image push $backendRegistry'
      }
    }
    // stage ('Frontend Docker Push') {
    //   steps {
    //     // Frontend Docker Push
    //     sh 'docker image push $frontendRegistry'
    //   }
    // }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}