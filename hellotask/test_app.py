from app import helloworld, getname, lastname

def hello():
    response = helloworld.test_client().get("/hello")
    assert response.data == b'Hello World'
    

def getname():
    response = getname.test_client().get("/getname")
    assert response.data == b'Prashant'

def lastaname():
    response = lastname.test_client().get("/thirdapi")
    assert response.data == b'Finally Task Completed'
