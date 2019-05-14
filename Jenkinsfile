node {
    checkout scm
    /* .. snip .. */
}
node {
    stage('Build') {
        sh 'make'
        archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
    }
}
node {
    /* .. snip .. */
    stage('Test') {
        /* `make check` returns non-zero on test failures,
         * using `true` to allow the Pipeline to continue nonetheless
         */
        sh 'make check || true'
        junit '**/target/*.xml'
    }
    /* .. snip .. */
}

node {
    /* .. snip .. */
    stage('Deploy') {
        if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
            sh 'make publish'
        }
    }
    /* .. snip .. */
}