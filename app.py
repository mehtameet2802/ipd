
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)
<<<<<<< HEAD
=======
pickle_in = open("CropRecommendation.pkl", "rb")
recommender = pickle.load(pickle_in)
recommender = decompress_pickle("Recommendation.pbz2")


@app.route("/check")
def index():
    return 'Hello, World. Website is working'


@app.route("/predict", methods=['POST'])
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
>>>>>>> 1dd12522585390b08a40fe45578b17dd0ada5e2f

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

