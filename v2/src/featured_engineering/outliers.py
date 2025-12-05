import pandas as pd
import numpy as np


def iqr_score(df, feature) :
    Q3 = df[feature].quantile(0.75)
    Q1 = df[feature].quantile(0.25)

    IQR = Q3 - Q1

    return IQR, Q3, Q1