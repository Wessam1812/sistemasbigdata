from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("modelo.pkl", "rb"))

@app.route("/predict", methods=["GET"])
def predict():
    promocion = float(request.args.get("promocion"))
    temperatura = float(request.args.get("temperatura"))
    dia_semana = float(request.args.get("dia_semana"))
    mes = float(request.args.get("mes"))

    data = np.array([[promocion, temperatura, dia_semana, mes]])
    prediction = model.predict(data)

    return jsonify({"prediccion": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)