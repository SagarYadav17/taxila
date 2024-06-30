pipeline {
  agent any
  environment {
    IMAGE_REPO_NAME = 'taxila'
    IMAGE_TAG = "${env.GIT_COMMIT}"
  }

  stages {
    stage('Test Code') {
      steps {
        echo 'Testing the code....'
      }
    }

    stage('Building image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_REPO_NAME}:${IMAGE_TAG}", '-f ./Dockerfile .')
        }
      }
    }
  }
}
