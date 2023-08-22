import json
import pickle
import numpy as np
__location=None
__data_columns=None
__model=None

def  get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1
    
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def get_location_names():
    load_saved_artifacts()
    return __location

def load_saved_artifacts():
    print("loading saved artifacts....start")
    global __data_columns
    global __location

    with open("./server/artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __location = __data_columns[3:]
    global __model    
    with open("./server/artifacts/bengaluru_house_prices.pickel",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts.....done")        


if __name__=='__main__':
    load_saved_artifacts()
