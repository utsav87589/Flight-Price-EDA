import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


### function to split the data
def split_data(df, target_feature) : 
        
        X = df.drop(target_feature, axis = 1)
        y = df[target_feature]

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = 0.25)

        return X_train, X_test, y_train, y_test


### function to verify the split (shapes basically)
def verify_split(X_train, X_test, y_train, y_test) : 
        
        print(f"X_train : {X_train.shape} :: y_train : {y_train.shape} \nX_test : {X_test.shape} :: y_test : {y_test.shape}")