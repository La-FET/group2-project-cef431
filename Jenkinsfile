pipeline {
    agent any

    // Check GitHub for new commits every 5 minutes.
    // (If you set up a GitHub webhook instead, you can remove this block.)
    triggers {
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v --junitxml=test-results.xml
                '''
            }
        }
    }

    post {
        always {
            // Publish test results so Jenkins shows pass/fail counts and trends
            junit 'test-results.xml'
        }
        success {
            echo 'All tests passed - build is GREEN.'
        }
        failure {
            echo 'Build FAILED - check the test results above.'
        }
    }
}
