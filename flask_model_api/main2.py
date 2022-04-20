from copyreg import pickle
from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
Swagger(app)

pickled_model_file = open("pickle_model.pkl", "rb")
regressor = pickle.load(pickled_model_file)

@app.route('/')
def home():
    return "Welcome to Diabetes centre"

@app.route('/predict') 
def predict_flower():

    """ Lets try Swagger from Flasgger
        ---
    parameters:
        - name: feature1
          in: query
          type: string
          required: true
        - name: feature2
          in: query
          type: string
          required: true
        - name: feature3
          in: query
          type: string
          required: true
        - name: feature4
          in: query
          type: string
          required: true
        - name: feature5
          in: query
          type: string
          required: true
        - name: feature6
          in: query
          type: string
          required: true
        - name: feature7
          in: query
          type: string
          required: true
        - name: feature8
          in: query
          type: string
          required: true
        - name: feature9
          in: query
          type: string
          required: true
        - name: feature10
          in: query
          type: string
          required: true      
    responses:
        200:
            description: the result is
    """
    f1 = request.args.get("feature1")
    f2 = request.args.get("feature2")
    f3 = request.args.get("feature3")
    f4 = request.args.get("feature4")
    f5 = request.args.get("feature5")
    f6 = request.args.get("feature6")
    f7 = request.args.get("feature7")
    f8 = request.args.get("feature8")
    f9 = request.args.get("feature9")
    f10 = request.args.get("feature10")

    result = regressor.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]])

    return f"The diabetes prediction is {result}"

if __name__ == "__main__":
    app.run()
