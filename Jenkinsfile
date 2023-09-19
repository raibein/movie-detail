pipeline {
  agent any
  stages {
    stage ('Fetch Git') {
      steps {
        git branch: 'automate', credentialsId: 'gitAuth', url: 'https://github.com/raibein/movie-detail.git'
      }
    }
    stage ('Build') {
      steps {
        // build
        echo 'bundle exec rake build'
      }
    }
    stage ('Test') {
      steps {
        // run tests with coverage
        echo 'bundle exec rake spec'
      }
    }
  }
}