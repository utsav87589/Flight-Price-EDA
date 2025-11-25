import pandas as pd
import numpy as np

def value_counts(df, cols) : 
    values = {}
    for col in cols : 
        values[col] = df[col].value_counts()
    return values

def one_hot(df, cols) : 
    for col in cols : 
        dummies = pd.get_dummies(df[col], dtype = int, drop_first = True, prefix = col)
        df = pd.concat([df, dummies], axis = 1)
    return df

# def label_encoding(df, cols, mapping) : 
#     for col in cols : 
#         df[col] = df[col].apply(mapping)
#     return df

