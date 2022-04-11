from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my name/<name>")
def print_name(name):
    return f"ma anna pulihora raja {name}"

@app.route("/hello",methods = ["GET","POST"])
def hello():
    stu_name = request.args.get("StudentName")
    numb = request.args.get("RollNo")
    return f"Student Name is {stu_name} and roll number is {numb}"

if __name__=="__main__":
    app.run()