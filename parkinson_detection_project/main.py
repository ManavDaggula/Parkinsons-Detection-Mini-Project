# flask, scikit-learn, pandas, pickle-mixin
import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)
data = pd.read_csv('parkinsons.csv')
pipe = pickle.load(open("model_svm.pkl", 'rb'))



@app.route('/')
def index():
    return render_template("index.html")

@app.post('/predict')
def get_results():
    print(request.form["fo"])
    return ""

# @app.route('/predict', methods=['POST'])

if __name__ == "__main__":
    app.run(debug=True, port=5000)

