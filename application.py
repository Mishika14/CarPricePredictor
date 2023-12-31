import pickle
from flask import Flask, render_template,request,render
import pandas as pd
import pickle
app = Flask(__name__)
model= pickle.load(open("LinearRegressionModel.pkl", 'rb'))
car=pd.read_csv("Cleaned Car.csv")
@app.route('/')
def index():
    comapnies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique())

    fuel_type=(car['fuel_type'].unique())
    return render('index.html',companies=comapnies,car_models=car_models,years=year,fuel_type=fuel_type)
@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('car_model')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    kms_driven=int(request.form.get('kilo_driven'))
    print(company,car_model,year,fuel_type,kms_driven)
    prediction=model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))
    return str(prediction[0]);
if __name__ ==  '__main__':
    app.run(debug=True)
