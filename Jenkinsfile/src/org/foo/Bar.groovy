// src/org/foo/Bar.groovy
package org.foo

def start(){
    stage('Build'){
        echo 'start build'
    }
    stage('Test'){
        echo 'start test'
    }
    stage('Deploy'){
        echo 'start deploy'
    }
}

return this