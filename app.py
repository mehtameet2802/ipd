from flask import Flask, jsonify, request
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
import bz2file as bz2


def decompress_pickle(file):
    data = bz2.BZ2File(file, "rb")
    data = pickle.load(data)
    return data


app = Flask(__name__)
pickle_in = open("CropRecommendation.pkl", "rb")
recommender = pickle.load(pickle_in)
recommender = decompress_pickle("Recommendation.pbz2")


@app.route('/', methods=['GET'])
def index():
    return 'Hello, World'


@app.route('/predict', methods=['POST'])
def predict_crop():
    nitrogen = float(request.form['nitrogen'])
    phosphorus = float(request.form['phosphorus'])
    potassium = float(request.form['potassium'])
    sodium = float(request.form['sodium'])
    iron = float(request.form['iron'])
    zinc = float(request.form['zinc'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    recommended_crop = recommender.predict([[nitrogen, phosphorus, potassium,
                                             sodium, iron, zinc, temperature, humidity, ph, rainfall]])
    print(f"prediction = {recommended_crop}")
    return jsonify(recommended_crop=recommended_crop[0])


if __name__ == '__main__':
    app.run(debug=True)
