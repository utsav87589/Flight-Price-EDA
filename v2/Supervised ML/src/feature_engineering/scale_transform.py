import pandas as pd
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import MinMaxScaler
import joblib


### function to apply boxcox transformation to the feature
def apply_transform_boxcox(df, cols) : 

    for col in cols : 
        df[col], parameter = boxcox(df[col] + 1)