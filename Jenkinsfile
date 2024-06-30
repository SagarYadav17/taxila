/* Requires the Docker Pipeline plugin */
pipeline {
  agent any
  environment {
    IMAGE_REPO_NAME = 'taxila'
    IMAGE_TAG = "${env.GIT_COMMIT}"
  }

  stages {
    stage('Test Code') {
      agent {
        docker {
            image 'python:3.12'
            // Run the container on the node specified at the
            // top-level of the Pipeline, in the same workspace,
            // rather than on a new node entirely:
            reuseNode true
            args '-v /root/.cache/pip:/root/.cache/pip'
        }
      }
      steps {
        echo 'Testing the code....'
        // pip install -r requirements.txt
        sh 'pip install -r requirements.txt'
        // run tests
        sh 'cd app && python manage.py test'
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
