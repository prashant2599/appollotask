from flask import Flask
import random
import requests
app = Flask(__name__)

@app.route("/hello")
def helloworld():
    data = "hello World"
    api_url="http://127.0.0.1:5000/thirdapi"
    response = requests.get(api_url)
    sub =  response.text
    return data+"  "+sub
    


@app.route("/getname")
def getname():
    with open('name.txt', 'r') as f:
        return random.choice(open('name.txt', 'r').readline().split())
    
@app.route("/thirdapi")
def lastname():
    return "Finally Compeleted"
        
if __name__ == "__main__":
            app.run(host= '0.0.0.0')
