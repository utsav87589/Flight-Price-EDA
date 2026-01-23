import pandas as pd
import numpy as np


### function to check the value counts and nunique values inside the categorical features
def get_nunique_value_counts(df, cols) : 

    for col in cols : 
        print(f"{df[col].nunique()} \n{df[col].value_counts()}")


### function to apply the one hot encoding to the features

def apply_one_hot(df, cols) : 

    for col in cols : 

        dummies = pd.get_dummies(df[col], dtype = int, prefix = col, prefix_sep = '_', drop_first = True)

        df = pd.concat([df, dummies], axis = 1)

        df.drop(col, axis = 1, inplace = True)

    return df



### function to apply the label encoding to the given column

