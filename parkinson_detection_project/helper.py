import pandas as pd
import numpy as np
import pickle

pipe = pickle.load(open("../pickle_files/plain/svm.model", 'rb'))
scaler = pickle.load(open("../pickle_files/plain/scaler.pkl","rb"))

def get_prediction(form_data):
    df = pd.DataFrame({0:form_data}).transpose()
    # print(df.columns)
    df = df.replace('',np.nan).astype(float)
    # df = df[df['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)','MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP','MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5','MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1','spread2', 'D2', 'PPE']]
    # df = df.iloc[:,[7,5,6,8,9,11,10,3,12,13,17,18,4,19,14,2,16,1,20,21,0,15]]
    df = df.loc[:,['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)','MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP','MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5','MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1','spread2', 'D2', 'PPE']]
    new_df = scaler.transform(df)
    print(new_df)
    output = pipe.predict(new_df)
    print(output)
    return output