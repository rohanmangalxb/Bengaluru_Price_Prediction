import json
import pickle
import numpy as np
import os

location_data = None
columns_data = None
model_data = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = columns_data.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(columns_data))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(model_data.predict([x])[0], 2)


def get_location_names():
    return location_data


def load_saved_artifacts():
    print("Loading saved artifacts...")

    global location_data
    global columns_data
    global model_data

    columns_path = os.path.join(BASE_DIR, "artifacts", "columns.json")
    model_path = os.path.join(BASE_DIR, "artifacts", "prediction_model.pickle")

    with open(columns_path, "r") as f:
        columns_data = json.load(f)["data_columns"]
        location_data = columns_data[3:]

    with open(model_path, "rb") as f:
        model_data = pickle.load(f)

    print("Artifacts loaded successfully!")
