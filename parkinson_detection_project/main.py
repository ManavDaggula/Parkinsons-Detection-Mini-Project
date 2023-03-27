# flask, scikit-learn, pandas, pickle-mixin
import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
data = pd.read_csv('parkinsons.csv')
pipe = pickle.load(open("model_svm.pkl", 'rb'))
scaler = pickle.load(open("scaler.pkl","rb"))


@app.route('/')
def index():
    return render_template("index.html")

@app.post('/predict')
def get_results():
    # print(request.form["mdvp_fo"])
    inp = [float(x) for x in request.form.values()]
    print("this is inp received : ",inp)


    inp = np.asarray([float(x) for x in request.form.values()])
    inp_reshaped = inp.reshape(1,-1)
    print(inp_reshaped)
    inp = scaler.transform(inp_reshaped)
    out = pipe.predict(inp_reshaped)
    print(out)

    return str(request.form)+"\n"+str(len(request.form.keys()))

@app.get("/test_model")
def test_model():
    input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)
    # input_data = (119.992,157.302,74.997,0.00784,0.00007,0.0037,0.00554,0.01109,0.04374,0.426,0.02182,0.0313,0.02971,0.06545,0.02211,21.033,0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654)
    # changing input data to a numpy array
    # print(type(input_data))
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the data
    std_data = scaler.transform(input_data_reshaped)

    prediction = pipe.predict(std_data)
    print(prediction)


    if (prediction[0] == 0):
        print("The Person does not have Parkinsons Disease")

    else:
        print("The Person has Parkinsons")
    return "done, now check terminal"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
