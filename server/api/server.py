from flask import Flask, request, jsonify
import util

app = Flask(__name__)

util.load_saved_artifacts()

@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    return jsonify({
        "locations": util.get_location_names()
    })

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    data = request.form

    total_sqft = float(data["total_sqft"])
    location = data["location"]
    bhk = int(data["bhk"])
    bath = int(data["bath"])

    estimated_price = util.get_estimated_price(
        location, total_sqft, bhk, bath
    )

    return jsonify({
        "estimated_price": estimated_price
    })