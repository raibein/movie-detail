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

        // Archive the built artifacts
        // archive includes: 'pkg/*.gem'
      }
    }
    stage ('Test') {
      steps {
        // run tests with coverage
        echo 'bundle exec rake spec'

        // publish html
        // publishHTML target: [
        //     allowMissing: false,
        //     alwaysLinkToLastBuild: false,
        //     keepAll: true,
        //     reportDir: 'coverage',
        //     reportFiles: 'index.html',
        //     reportName: 'RCov Report'
        //   ]
      }
    }
  }
}