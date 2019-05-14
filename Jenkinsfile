node {
    checkout scm
    /* .. snip .. */
}
node {
    stage('Build') {
        bat 'echo start Build'
        //archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
    }
}
node {
    /* .. snip .. */
    stage('Test') {
        withEnv(["robot_path=tc"]){
        bat 'dir tc'
        }

        bat 'echo start Test'
        // Using returnStdout
        CC = """${bat(
                returnStdout: true,
                script: 'echo "clang"'
            )}"""
        echo CC

         // Using returnStatus
        EXIT_STATUS = """${bat(
                returnStatus: true,
                script: 'exit 1'
            )}"""
        echo EXIT_STATUS

        echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
        def username = 'Jenkins'
        echo 'Hello Mr. ${username}'
        echo "I said, Hello Mr. ${username}"
    }

}

node {
    /* .. snip .. */
    stage('Deploy') {

        if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
            bat 'echo start Deploy'
            //bat 'robot --pythonpath . tc'
        }
    }

}