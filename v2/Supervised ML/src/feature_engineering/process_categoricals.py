import pandas as pd
import numpy as np


### function to check the value counts and nunique values inside the categorical features
def get_nunique_value_counts(df, cols) : 

    for col in cols : 
        print(f"{df[col].unique()} \n{df[col].value_counts()}")