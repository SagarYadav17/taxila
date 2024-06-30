/* Requires the Docker Pipeline plugin */
pipeline {
  agent any
  environment {
    IMAGE_REPO_NAME = 'taxila'
    IMAGE_TAG = "${env.GIT_COMMIT}"
  }

  stages {
    // Building Docker images
    stage('Building image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_REPO_NAME}:${IMAGE_TAG}", '-f ./Dockerfile_test .')
        }
      }
    }
  }

  post {
    always {
      echo 'This will always run'
    }
    success {
      echo 'This will run only if successful'
    }
    failure {
      echo 'This will run only if failed'
    }
    unstable {
      echo 'This will run only if the run was marked as unstable'
    }
    changed {
      echo 'This will run only if the state of the Pipeline has changed'
      echo 'For example, if the Pipeline was previously failing but is now successful'
    }
  }
}
