stage('Build') {
    node {
        checkout scm
        bat 'echo make'
        //stash includes: '**/target/*.jar', name: 'app'
    }
}

stage('Test') {
    node('linux') {
        checkout scm
        try {
            //unstash 'app'
            sh 'echo makecheck'
        }
        finally {
            //junit '**/target/*.xml'
            echo 'linux done'
        }
    }
    node('windows') {
        checkout scm
        try {
            //unstash 'app'
            bat 'echo makecheck'
        }
        finally {
            //junit '**/target/*.xml'
            echo 'windows done'
        }
    }
}