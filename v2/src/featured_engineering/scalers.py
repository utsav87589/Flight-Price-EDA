import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

scaler = MinMaxScaler(feature_range = (0, 1))

#------------- function to apply the Min max scaler and then saving it
def scale_feature(df, cols) : 
   #----------applying the scaler
    df[cols] = scaler.fit_transform(df[cols])

    #---------saving the scaler according to the column it was applied on
    if 'Price' in cols : 
     scaler_path = '../../scalers/scaler_for_price.pkl'
     joblib.dump(scaler, scaler_path)

    else : 
     scaler_path = '../../scalers/scaler_for_rest.pkl'
    joblib.dump(scaler, scaler_path)