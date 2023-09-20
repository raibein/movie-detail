// Here the Frontend is not going to build Dockerfile and push to Docker Hub
// The resource cannot handle this much space, that's mean the out of space.
// The AWS is free teir, so this Jenkins host could not handle the much packages of the Frontend.
// That is why I have commented the frontend docker file and also commented to push docker file.


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