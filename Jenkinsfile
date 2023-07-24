pipeline {

   agent any

   stages {

     stage('checkout from scm') {

       steps {

      checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '53892fa2-7365-4d8a-b98c-a7f0f8a084b1', url: 'https://github.com/kiran260790/python_basic_scripting.git']])
}

       }
       }
     }
