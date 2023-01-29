
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
    nitrogen = st.number_input('nitrogen')
    phosphorus = st.number_input('phosphorus')
    potassium = st.number_input('potassium')
    sodium = st.number_input('sodium')
    iron = st.number_input('iron')
    zinc = st.number_input('zinc')
    temperature = st.number_input('temperature')
    humidity = st.number_input('humidity')
    ph = st.number_input('ph')
    rainfall = st.number_input('rainfall')

    recommended_crop = ''
    if st.button('Predict Crop'):
        recommended_crop = recommender.predict([[nitrogen, phosphorus, potassium,
                                                 sodium, iron, zinc, temperature, humidity, ph, rainfall]])
    print(f"prediction = {recommended_crop}")
    st.success(recommended_crop[0])


if __name__ == '__main__':
    main()
