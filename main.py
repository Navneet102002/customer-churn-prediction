from flask import Flask, request, jsonify, render_template
from server import util
from waitress import serve

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("app.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_churn', methods=['GET', 'POST'])
def predict_churn():
    bill = float(request.form['bill'])
    gb_used = float(request.form['gb_used'])
    location = request.form['location']
    age = int(request.form['age'])
    sub_months = int(request.form['sub_months'])
    gender = int(request.form['gender'])

    response = jsonify({
        'estimated_churn': util.get_estimated_churn(age, sub_months, bill, gb_used, gender, location)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    print("Starting Python flask server for Customer Churn Prediction")
    util.load_saved_artifacts()
    # app.run(port=80)
    serve(app, host='0.0.0.0', port=80) # remove port attribute to use 5000 port or just run app.run(). Alos use this for ec2 deployment