import pandas as pd
import numpy as np

#-------------function to load the data, based on the path given
def load_data(df_path) : 
    df = pd.read_csv(df_path)
    return df


#--------------function to perform initial check : nan values
def get_nan(df) : 
    return df.isna().sum()


#--------------function to perform initial check : get_info
def get_info(df) : 
    return df.info()

