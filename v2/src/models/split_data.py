#---------------splitting the data and returning the train/test files

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#------------function to split the data
#------------if it has price column, then it is regular data else, it's test data as x_eval
def data_split(df, price = None) : 
    #------------if price column is there
    if price is not None : 
        X = df.drop('Price', axis = 1)
        y = df['Price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = 0.25)
        return X_train, X_test, y_train, y_test
        

    #-----------if price column in not there
    else : 
        X_eval = df
        return X_eval