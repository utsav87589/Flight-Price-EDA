import pandas as pd
import numpy as np


### function to check for the values, in a different format in the given numerical column
def get_format(df, col, patterns) : 

    print(df[col].astype(str).str.len().value_counts())
    print(f"total records : {df.shape[0]}")


    for name, pat in patterns.items():
        count = df[col].astype(str).str.match(pat).sum()
        print(name, ":", count)


### function to split the features, based on the operator given
def split_numericals(df, col, sep, new_cols) : 

    #-------------splitting based on the given operator

    split_df = df[col].str.split(sep, expand = True)

    for i in range(split_df.shape[1]) : 
        df[f"{new_cols[i]}"] = split_df[i]

    #-----------then dropping the old column

    df.drop(col, axis = 1, inplace = True)


### function to check the unique values i.e. sometimes after split, we might wanna drop the further column, if it has no diversity
def check_value_counts_numericals(df, cols) : 

    for col in cols : 
        print(f"{df[col].nunique()} \n{df[col].value_counts()}")


### function to drop the column from the newly created numerical columns
def drop_cols_numerical(df, col) : 
    
    df.drop(col, axis = 1, inplace = True)
