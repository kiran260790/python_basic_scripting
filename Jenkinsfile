pipeline {

   agent any

   stages {

     stage('checkout from scm') {

       steps {

      withCredentials([gitUsernamePassword(credentialsId: '53892fa2-7365-4d8a-b98c-a7f0f8a084b1', gitToolName: 'Default')]) {
      sh 'ls'
}

       }
       }
     }
}
