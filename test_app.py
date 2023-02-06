try:
    from app import app
    import unittest

except Exception as e:
    print("some modules are missing {} ".format(e))

class FlaskTest(unittest.TestCase):

    def test_helloworld(self):
        tester = app.test_client(self)
        response = tester.get('/hello')
        text = response.text
        # statuscode = response.status_code
        self.assertEqual(text, 'hello World  Finally Compeleted')


    # def test_getname(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/getname')
    #     statuscode = response.status_code
    #     # text = response.text
    #     self.assertEqual(statuscode, 200)

    def test_lastname(self):
        tester = app.test_client(self)
        response = tester.get('/thirdapi')
        statuscode = response.status_code
        # text = response.text
        self.assertEqual(statuscode, 200)
           
if __name__ == "__main__":
    unittest.main()        
