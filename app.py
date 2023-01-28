import uvicorn
from fastapi import FastAPI
from soilAttributes import SoilData
import numpy as np
import pandas as pd
import pickle
import bz2file as bz2


def decompress_pickle(file):
    data = bz2.BZ2File(file, "rb")
    data = pickle.load(data)
    return data


app = FastAPI()
pickle_in = open("CropRecommendation.pkl", "rb")
recommender = pickle.load(pickle_in)
recommender = decompress_pickle("Recommendation.pbz2")
# data = bz2.BZ2File("Recommendation.pbz2", "rb")
# recommender = pickle.load(model)


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
