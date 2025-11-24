import pandas as pd
import numpy as np

def value_counts(df, cols) : 
    values = {}
    for col in cols : 
        values[col] = df[col].value_counts()
    return values

def one_hot(df, cols) : 
    for col in cols : 
        col = pd.get_dummies(df[col], dtype = int, drop_first = True, prefix = col)
        df = pd.concat([df, col], axis = 1)
    return df
