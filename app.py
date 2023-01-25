import uvicorn
from fastapi import FastAPI
from soilAttributes import SoilData
import numpy as np
import pandas as pd
import pickle


app = FastAPI()
pickle_in = open("CropRecommendation.pkl", "rb")
recommender = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict_crop(data: SoilData):
    data = data.dict()
    nitrogen = data['nitrogen']
    phosphorus = data['phosphorus']
    potassium = data['potassium']
    sodium = data['sodium']
    iron = data['iron']
    zinc = data['zinc']
    temperature = data['temperature']
    humidity = data['humidity']
    ph = data['ph']
    rainfall = data['rainfall']
    recommended_crop = recommender.predict([[nitrogen, phosphorus, potassium,
                                             sodium, iron, zinc, temperature, humidity, ph, rainfall]])
    print(f"input data = {data}")
    print(f"prediction = {recommended_crop}")
    return {'recommended_crop': recommended_crop[0]}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
