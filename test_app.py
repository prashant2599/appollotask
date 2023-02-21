from app import helloworld

try:
    from app import app
    import unittest

except Exception as e:
    print("some modules are missing {} ".format(e))

class FlaskTest(unittest.TestCase):

#first test case
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/')
        text1 = response.text
        # statuscode = response.status_code
        self.assertEqual(text1, 'hello world')

#second testcase
    def test_getname(self):
        tester = app.test_client(self)
        response = tester.get('/getname')
        statuscode = response.status_code
        # text = response.text
        self.assertEqual(statuscode, 200)

#third testcase
    def test_lastname(self):
        tester = app.test_client(self)
        response = tester.get('/thirdapi')
        statuscode = response.status_code
        # text = response.text
        self.assertEqual(statuscode, 200)
#fourth testcase
    def test_mixcase1(self):
        tester = app.test_client(self)
        response1 = helloworld()
        self.assertEqual(response1, 'hello world Finally Compeleted')

     
if __name__ == "__main__":
    unittest.main()        
