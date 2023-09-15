from flask import Flask
import random
import requests
app = Flask(__name__)


@app.route('/')
def hello():
    data = "hello world"
    return data

# @app.route("/hello")
# def helloworld():
#     # res = hello()
#     api_url = "http://127.0.0.1:5000/thirdapi"
#     res1 = requests.get(api_url)
#     sub =  res1.text
#     return hello()+" "+sub

# @app.route("/getname")
# def getname():
#     with open('name.txt', 'r') as f:
#         return random.choice(open('name.txt', 'r').readline().split())

# @app.route("/thirdapi")
# def lastname():
#     return "Finally Task Completed"        

        
if __name__ == "__main__":
            app.run(host='0.0.0.0')
