import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
import scipy.cluster.hierarchy as sc
from sklearn.neighbors import NearestNeighbors

#---------------function to plot the results like graphs and silhouette score
def results(df, y_labels) : 
    print(silhouette_score(df, y_labels))
    plt.figure(figsize = (8, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(df[:, 0], df[:, 1], c = y_labels)
    plt.subplot(1, 2, 2)
    plt.scatter(df[:, 0], df[:, 1])
    plt.show()



#========================= Kmeans clustering =========================

#------------function to find the k for Kmeans clustering
def find_k(df) : 
    wcss = []

    for k in range(1, 12) : 
        kmeans = KMeans(n_clusters = k, init = 'k-means++')
        kmeans.fit(df)
        wcss.append(kmeans.inertia_)

    print(wcss)
    plt.plot(range(1, 12), wcss)
