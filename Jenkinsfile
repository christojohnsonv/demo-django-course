pipeline{
  agent any
  stages{
    stage('Setup Python Virtual environment'){
      steps{
        sh '''
        chmod +x envsetup.sh
        ./envsetup.sh
        '''
      }
    }
    stage('Setup Gunicorn Setup'){
      steps{
        sh '''
          chmod +x gunicorn.sh
          ./gunicorn.sh
        '''
      }
    }
    stage('Setup NGINX'){
      steps{
        sh '''
          chmod +x nginx.sh
          ./nginx.sh
          '''
      }
    }
  }
}