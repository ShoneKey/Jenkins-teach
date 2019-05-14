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
        /* `make check` returns non-zero on test failures,
         * using `true` to allow the Pipeline to continue nonetheless
         */
        bat 'echo start Test'
        //junit '**/target/*.xml'
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
            bat 'robot --pythonpath . tc'
        }
    }
    /* .. snip .. */
}