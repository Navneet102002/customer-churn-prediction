import json
import pickle
import numpy as np

__data_columns = None
__locations = None
__model = None

def get_estimated_churn(age, sub_months, bill, gb_used, gender, location):
    try:
        loc_ind = __data_columns.index(location.lower())
    except:
        loc_ind = -1

    x = np.zeros(len(__data_columns))
    x[0] = age
    x[1] = sub_months
    x[2] = bill
    x[3] = gb_used
    x[4] = gender
    if loc_ind>=0:
        x[loc_ind] = 1
    
    return True if round(__model.predict([x])[0]) else False

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts.....start")
    global __data_columns
    global __locations
    global __model

    with open("./server/artifacts/columns.json", 'r') as f:
        cur = json.load(f)
        __data_columns = cur['data_columns']
        __locations = cur['data_locs']
    
    with open("./server/artifacts/churn_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts.....done")

if __name__=="__main__":
    load_saved_artifacts()
    print(__data_columns)
    print(__locations)