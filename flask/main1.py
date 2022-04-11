from flask import Flask

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my name")
def print_name():
    return "ma anna prathyush pulihora raja"

if __name__=="__main__":
    app.run()