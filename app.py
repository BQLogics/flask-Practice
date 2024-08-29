# from flask import Flask , request, render_template
# app = Flask (__name__,template_folder="templates")

# @app.route("/")
# def index():
#     mylist=[1,2,3,4,5]
#     return render_template("index.html",mylist=mylist)

# @app.route("/greeting/<name>")
# def greeting(name):
#     return f"Hell Good evening {name}"

# # @app.route ("/summation/<int:num1>/<int:num2>")
# # def sum(num1,num2):
# #     return f"{num1} + {num2} = {num1+num2}"

# # @app.route ('/url_params')
# # def params():
# #     return str(request.args)

# # @app.route("/home")
# # def home():
# #     return f"this is another test6"

# if __name__ == "__main__":
#     app.run (debug=True)


from flask import Flask
app = Flask(__name__)


@app.route('/greeting/<name>')
def greeting(name):
    return f"hello goodafternoon {name}"

@app.route("/<int:num1>/<int:num2>")
def summation(num1,num2):
    return f"{num1}+{num2}={num1+num2}"


if __name__ == '__main__':
    app.run(debug=True)