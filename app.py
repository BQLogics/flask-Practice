from flask import Flask , request
app = Flask (__name__)

@app.route("/")
def index():
    return "<h3>this is test 5</h3>"

@app.route("/greeting/<name>")
def greeting(name):
    return f"Hell Good evening {name}"

@app.route ("/summation/<int:num1>/<int:num2>")
def sum(num1,num2):
    return f"{num1} + {num2} = {num1+num2}"

@app.route ('/url_params')
def params():
    return str(request.args)

@app.route("/home")
def home():
    return f"this is another test6"

if __name__ == "__main__":
    app.run (debug=True)
