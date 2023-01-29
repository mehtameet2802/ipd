
# A very simple Flask Hello World app for you to get started with...

import pickle
import bz2file as bz2
import streamlit as st


def decompress_pickle(file):
    data = bz2.BZ2File(file, "rb")
    data = pickle.load(data)
    return data


recommender = decompress_pickle("Recommendation.pbz2")


def main():
    st.title('Crop Recommendation')
    nitrogen = float(st.number_input('nitrogen'))
    phosphorus = float(st.number_input('phosphorus'))
    potassium = float(st.number_input('potassium'))
    sodium = float(st.number_input('sodium'))
    iron = float(st.number_input('iron'))
    zinc = float(st.number_input('zinc'))
    temperature = float(st.number_input('temperature'))
    humidity = float(st.number_input('humidity'))
    ph = float(st.number_input('ph'))
    rainfall = float(st.number_input('rainfall'))

    recommended_crop = ''
    if st.button('Predict Crop'):
        recommended_crop = recommender.predict([[nitrogen, phosphorus, potassium,
                                                 sodium, iron, zinc, temperature, humidity, ph, rainfall]])
    print(f"prediction = {recommended_crop}")
    st.success(recommended_crop[0])


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


if __name__ == '__main__':
    main()
