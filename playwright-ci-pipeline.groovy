pipeline {
    agent any
    environment {
        PYTHON_ENV = ".venv"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/possible_username/python_playwright.git'
            }
        }
        stage('Setup') {
            steps {
                sh '''
                pip install -r requirements.txt
                playwright install
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source ${PYTHON_ENV}/bin/activate
                pytest --html=report.html --self-contained-html
                '''
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
