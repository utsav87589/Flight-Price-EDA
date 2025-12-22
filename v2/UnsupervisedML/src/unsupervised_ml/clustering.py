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

#-----------function to plot the scatter plots for the value of the k
def kmeans_clutsers(df, k) : 

    kmeans = KMeans(n_clusters = k, init = 'k-means++')
    y_labels = kmeans.fit_predict(df)

    results(df, y_labels = y_labels)


#========================= DBScan clustering =========================

#-------------function to find the value of eps
def find_eps(df) : 

    neigh = NearestNeighbors(n_neighbors = 5)
    nbrs = neigh.fit(df) 
    distances, indices = neigh.kneighbors(df)

    distances = np.sort(distances[:, 4])

    plt.plot(distances)

#------------function to plot the clusters for the value of eps
def db_clusters(df, eps) : 
    db_scan = DBSCAN(eps = eps)
    y_labels_db = db_scan.fit_predict(df)

    results(df, y_labels = y_labels_db)


#========================= HM clustering =========================

#-----------------function to make sample of 3000 records from the original data for the hm
def sample_for_hm (df, n_samples = 3000, random_state = 42) : 
    return df.sample(n = n_samples, random_state = random_state)

#----------------function to plot dendogram for the value of k
def plot_dendo(df_hm) : 
    plt.figure(figsize=(20,7))
    plt.title("Dendogram")
    sc.dendrogram(sc.linkage(df_hm, method = 'ward'))
    plt.title('Dendogram')
    plt.xlabel("sample index")
    plt.ylabel("euclidian distance")