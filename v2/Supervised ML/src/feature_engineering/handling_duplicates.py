import pandas as pd
import numpy as np


### function to check the number of duplicates and show the duplicate records
def get_duplicates(df) : 

    # print(f"{df.duplicated().sum()} \n{df[df.duplicated(keep = False)]}")
    return df[df.duplicated(keep = False)]