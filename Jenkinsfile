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
    }
    /* .. snip .. */
}

node {
    /* .. snip .. */
    stage('Deploy') {
        if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
            bat 'echo start Deploy'
        }
    }
    /* .. snip .. */
}