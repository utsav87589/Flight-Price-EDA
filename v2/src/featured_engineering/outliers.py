import pandas as pd
import numpy as np

#-----------function to calculate and return the iqr score for the given feature
def iqr_score(df, feature) :

    values = []

    Q3 = df[feature].quantile(0.75)
    values.append(Q3)

    Q1 = df[feature].quantile(0.25)
    values.append(Q1)

    IQR = Q3 - Q1
    values.append(IQR)

    return values


#--------------function to take upper and lower limit values and then apply it on the feature
def adjust_values(df, feature, lower_limit, upper_limit) : 

    df[feature] = df[feature].apply(lambda x : upper_limit if x > upper_limit else x)
    df[feature] = df[feature].apply(lambda x : lower_limit if x < lower_limit else x)