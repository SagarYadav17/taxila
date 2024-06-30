/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker }
    environment {
        IMAGE_REPO_NAME = 'taxila'
        IMAGE_TAG = "${env.GIT_COMMIT}"
    }

    stage('Unit Tests') {
      steps {
        script {
          sh 'pip freeze'
        }
      }
    }

    // Building Docker images
    stage('Building image') {
      steps {
        script {
          dockerImage = docker.build("${IMAGE_REPO_NAME}:${IMAGE_TAG}", '-f ./Dockerfile .')
        }
      }
    }
}
