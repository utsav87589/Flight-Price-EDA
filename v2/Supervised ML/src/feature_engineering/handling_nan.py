import pandas as pd
import numpy as np


### function to return the location of the nan values
def get_nan_location(df, col) : 

    return df[df[col].isna() == True]


### function to drop the entire row containing the nan
def drop_nan_record(df, record_index) :

    df.drop(record_index, axis = 0, inplace = True)

    df = df.reset_index(drop = True)

    return df