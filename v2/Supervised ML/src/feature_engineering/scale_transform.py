import pandas as pd
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import MinMaxScaler
import joblib


### function to apply boxcox transformation to the feature
def apply_transform_boxcox(df, cols) : 

    for col in cols : 
        df[f"{col}_boxcox"], parameter = boxcox(df[col] + 1)


### function to drop the old/new columns, if the transformation worked or not
def drop_pre_post_transformation(df, cols) : 
    
    df.drop(cols, axis = 1, inplace = True)


### function to scale the data and save the scaler on the train data.
def scale_train(df, cols_to_scale, scaler_path) : 

    scaler = MinMaxScaler(feature_range = (0, 1))

    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    joblib.dump(scaler, scaler_path)


### function to scale the valid data, by loading the scaler that was already fit on the train data
def scale_valid(df, cols_to_scale, scaler_path) : 

    scaler = joblib.load(scaler_path)
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])