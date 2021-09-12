def buildApp() {
    echo 'building from script'
}

def testApp() {
    echo 'Testing from script'
    sh "python3 test_app.py"
}
return this

