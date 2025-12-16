import pandas as pd
import numpy as np


#--------------return the unique values in a column
def unique_values(df, col) : 
    return df[col].unique()


#--------------return the value counts of the column
def value_counts(df, col) : 
    return df[col].value_counts()


#-------------one hot encoding for the categorical columns
def one_hot(df, col) : 
    dummies = pd.get_dummies(df[col], dtype = int, drop_first = True, prefix = col)
    df = pd.concat([df, dummies], axis = 1)
    return df


#-------------label encoding for the categorical columns
def label_encoding(df, col, mapping) : 
    df[col] = df[col].map(mapping)
    return df


#---------------spliting the numerical column like Date_of_journey, Dep_time etc..
def split_numerical(df, col) : 

    sample_value = str(df[col].iloc[0])

    if '/' in sample_value : 
        sep = '/'
        new_cols = ['day', 'month', 'year']

    elif ':' in sample_value : 
        sep = ':'
        new_cols = ['hour', 'minute']

    elif 'h' or 'm' in sample_value : 
        sep = 'h'
        new_cols = ['in_hours', 'in_minutes']

    else : 
        raise ValueError((f"{col} doesn't conatin '/' or ':'"))
    
    split_df = df[col].str.split(sep, expand = True)

    for i in range(split_df.shape[1]) : 
        df[f"{col}_{new_cols[i]}"] = split_df[i]

    return df


#------------------splitting the numerical features further for columns like Arrival_Time_minutes
def split_numerical_further(df, col) : 

    def extract_first(value) : 
        if not isinstance(value, str) : 
            return value
        return value.split()[0]
    
    df[col] = df[col].astype(str).apply(extract_first)

    return df


#---------------dropping the particular column
def columns_to_drop(df, cols) : 
    df.drop(cols, axis = 1, inplace = True)
    return df