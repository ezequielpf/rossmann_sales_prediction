import pandas as pd
import pickle
from flask import Flask, request, Response, jsonify
import json

from rossmann.Rossmann import Rossmann

# loading model
model = pickle.load(open('/home/ezequiel/Documentos/Prejetos_Data_Science/DS_em_producao/model/model_rossmann.pkl', 'rb'))

# initialize API
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():
     
    test_json = request.get_json()
   
    test_raw = pd.json_normalize(json.loads(test_json))

    pipeline = Rossmann()

    df1 = pipeline.data_cleaning(test_raw)
    df2 = pipeline.feature_engineering(df1)
    df3 = pipeline.data_preparation(df2)
    df_response = pipeline.get_prediction(model, test_raw, df3)
    return df_response

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=False)