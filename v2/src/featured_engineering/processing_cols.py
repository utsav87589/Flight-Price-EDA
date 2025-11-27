import pandas as pd
import numpy as np

def unique_values(df, col) : 
    return df[col].unique()

def value_counts(df, col) : 
    return df[col].value_counts()

def one_hot(df, col) : 
    dummies = pd.get_dummies(df[col], dtype = int, drop_first = True, prefix = col)
    df = pd.concat([df, dummies], axis = 1)
    return df

def label_encoding(df, col, mapping) : 
    df[col] = df[col].apply(mapping)
    return df

def columns_to_drop(df, cols) : 
    df.drop(cols, axis = 1, inplace = True)
    return df