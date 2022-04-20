from copyreg import pickle
from flask import Flask, request
import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

pickled_model_file = open("pickle_model.pkl", "rb")
regressor = pickle.load(pickled_model_file)

def predict_flower():
 
    try :
        st.title("Model Deployment")
        f1 = st.text_input("Feature 1 :")
        f2 = st.text_input("Feature 2 :")
        f3 = st.text_input("Feature 3 :")
        f4 = st.text_input("Feature 4 :")
        f5 = st.text_input("Feature 5 :")
        f6 = st.text_input("Feature 6 :")
        f7 = st.text_input("Feature 7 :")
        f8 = st.text_input("Feature 8 :")
        f9 = st.text_input("Feature 9 :")
        f10 = st.text_input("Feature 10 :")
       
        result = regressor.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]])
 
        if st.button("Print output"):
            st.success(result)
    except Exception as e :
        return f" Error occured with message : {e}"
 
if __name__=="__main__":
    predict_flower()