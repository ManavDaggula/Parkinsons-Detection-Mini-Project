# flask, scikit-learn, pandas, pickle-mixin
# import pandas as pd
import helper
from flask import Flask, render_template, request

import numpy as np
app = Flask(__name__)
# data = pd.read_csv('parkinsons.csv')



@app.route('/')
def index():
    return render_template("index.html")

@app.post('/predict')
def get_results():
    print(request.form)
    out = helper.get_prediction(request.form)
    pred = "You have parkinsons" if (out[0]==1) else  "You don't have parkinsons."
    return render_template("manav.html",pred=pred,values=request.form)
    # return pred
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)
