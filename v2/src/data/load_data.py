import pandas as pd
import numpy as np
import os

## Function to load the data

def load_data(file_path) : 

    """
    Load a data set from csv or excel file, based on it's type
    """

    #1. Check if file exist or not 
    if not os.path.exists(file_path) : 
        print(f"File not found : {file_path}")

    #2. extract file extension
    ext = os.path.splitext(file_path)[1].lower()

    #3. if the file is csv or excel file, load accordingly
    if ext == '.csv' : 
        return pd.read_csv(file_path)

    elif ext in ['.xlsx', '.xls'] : 
        return pd.read_excel(file_path)
    
    else : 
        raise ValueError(f"Unsupported file type : {ext}. Allowed : CSV, XLSX, XLS")
    
## Checking the shape of the data

def get_shape(df) : 
    return df.shape

def get_nan(df) : 
    return df.isna().sum()