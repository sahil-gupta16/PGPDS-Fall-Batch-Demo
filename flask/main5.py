from flask import Flask,request
from flasgger import Swagger ###

app = Flask(__name__)
Swagger(app)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my name/<name>")
def print_name(name):
    return f"happy learning {name} in praxis pulihora"

@app.route("/hello",methods = ["GET","POST"])
def hello():

    """ Lets try Swagger from Flasggger
    ---
    parameters:
        - name: StudentName
          in: query
          type: string
          required: true
        - name: RollNo
          in: query
          type: string
          required: true      
    responses:
        200:
            description: the result is
    """
    try:
        stu_name = request.args.get("StudentName")
        numb = request.args.get("RollNo")
        return f"Student Name is {stu_name} and roll number is {numb}",200
    
    except Exception as e:
        return f"Error occured with message : {e}",401


if __name__=="__main__":
    app.run()