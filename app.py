"""
@author: Awesh khan
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

#model.pkl is used to get the predictions on new data
# in this page np pd pickle we did not used it is masked


app=Flask(__name__)

pickle_in = open("C:\\Users\\Administrator\\Desktop\\Salary_program\\salary_predition.pkl", "rb")
model = pickle.load(pickle_in)



@app.route('/')      # decorator
def welcome():
    return "Hi this is my First Page"


@app.route('/predict',methods=["Get"])
def predict_salary():

    """
    ['YearsExperience']
   """
    input_cols=['YearsExperience']
    list1=[]
    for i in input_cols:
        val = request.args.get(i)
        list1.append(eval(val))


    prediction=model.predict([list1])
    pred=int(prediction[0])

    return "Your Expected Salary is : "+str(pred)


@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))  # whatever name you written here the same name will provide in Post man
    prediction=model.predict(df_test)
    return str(list(prediction))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)