import json, pickle, numpy as np


location_data = None
columns_data = None
model_data = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = columns_data.index(location.lower())
    except:
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
    print('Loading saved artifacts....')
    global location_data
    global columns_data
    global model_data

    with open("./server/artifacts/columns.json", 'r') as f:
        columns_data = json.load(f)['data_columns']
        location_data = columns_data[3:]
    
    with open("./server/artifacts/prediction_model.pickle", 'rb') as f:
        model_data = pickle.load(f)

    print("Loading of artifacts completed!")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 3))