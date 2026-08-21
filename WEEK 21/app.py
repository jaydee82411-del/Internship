from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open("model.pkl", 'rb') as file:
    model = pickle.load(file)

@app.route("/")
def home():
  return "ML model API is running"

@app.route("/predict", methods=["POST"])
def predict():

  data = request.json

  features = [[
      data["sepal_length"],
      data["sepal_width"],
      data["petal_length"],
      data["petal_width"]
  ]]

  prediction = model.predict(features)[0]

  return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
  app.run(debug=True)

