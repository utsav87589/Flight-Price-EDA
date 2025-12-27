import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.cluster import DBSCAN


### -------------Function to plot the outliers 
### -------------this function will be used implicitly only
def plot_anomalies(df, outliers) : 
    plt.figure(figsize = (8, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(df[:, 0], df[:, 1])
    plt.scatter(df[outliers, 0], df[outliers, 1], edgecolors = 'r')
    plt.subplot(1, 2, 2)
    plt.scatter(df[:, 0], df[:, 1])
    plt.show()


# ====================== Isolation forest =========================

#------------function to find the value of contamination
def find_threshold(df) : 

    cif = IsolationForest(contamination = 'auto', random_state = 42)
    cif.fit(df)

    scores = np.sort(cif.score_samples(df))

    print(scores)
    plt.plot(scores)

    return scores


#-------------function to take the value of the scores from the above function and then gives the number of value below that score
def find_contamination(df, scores, threshold) : 

    values = np.where(scores < threshold)
    contamination = 1.0 - ((len(df) - len(values[0])) / len(df))

    print(len(values[0]))
    print(contamination)

#------------function to plot the outliers based on the given value of the contamination
def outliers_isolation_forest(df, contamination) :

    cif = IsolationForest(contamination = contamination, random_state = 42)
    predictions = cif.fit_predict(df)

    outliers = np.where(predictions < 0)

    plot_anomalies(df, outliers)