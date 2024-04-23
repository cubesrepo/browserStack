pipeline{
    agent any
    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/browserStack'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m bstackVENV'
                bat 'bstackVENV\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'bstackVENV\\Scripts\\activate && pytest -v --html=report.html'
            }
        }
    }
}