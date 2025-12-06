import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

#------------- function to apply the Min max scaler and then saving it
def scale_feature(df, cols, scaler_path = None) : 
   #----------applying the scaler

  if scaler_path is None : 

    scaler = MinMaxScaler(feature_range = (0, 1))

    df[cols] = scaler.fit_transform(df[cols])

    #---------saving the scaler according to the column it was applied on
    if 'Price' in cols : 
     scaler_path = '../../../scalers/scaler_for_price.pkl'
     joblib.dump(scaler, scaler_path)

    else : 
      scaler_path = '../../../scalers/scaler_for_rest.pkl'
      joblib.dump(scaler, scaler_path)

  else : 
    scaler = joblib.load(scaler_path)
    df[cols] = scaler.fit_transform(df[cols])
