from app import helloworld, getname, lastname

def test_hello():
    response = helloworld.test_client().get("/hello")
    assert response.data == b'Hello World'
    

def test_getname():
    response = getname.test_client().get("/getname")
    assert response.data == b'Prashant'

def test_lastaname():
    response = lastname.test_client().get("/thirdapi")
    assert response.data == b'Finally Task Completed'
