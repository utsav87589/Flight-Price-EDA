import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
import scipy.cluster.hierarchy as sc
from sklearn.neighbors import NearestNeighbors

#---------------function to plot the results like graphs and silhouette score
### this function will be called implicitly only in this file
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
def kmeans_clutsers(df, k, labels_path = None) : 
    if labels_path is not None : 
        kmeans = KMeans(n_clusters = k, init = 'k-means++')
        y_labels_kmeans = kmeans.fit_predict(df)

        np.save(labels_path, y_labels_kmeans)

        results(df, y_labels = y_labels_kmeans)

    else : 
        kmeans = KMeans(n_clusters = k, init = 'k-means++')
        y_labels_kmeans = kmeans.fit_predict(df)

        results(df, y_labels = y_labels_kmeans)

#========================= DBScan clustering =========================

#-------------function to find the value of eps
def find_eps(df) : 

    neigh = NearestNeighbors(n_neighbors = 5)
    nbrs = neigh.fit(df) 
    distances, indices = neigh.kneighbors(df)

    distances = np.sort(distances[:, 4])

    plt.plot(distances)

#------------function to plot the clusters for the value of eps
def db_clusters(df, eps, labels_path = None) : 
    
    if labels_path is not None : 

        db_scan = DBSCAN(eps = eps)
        y_labels_db = db_scan.fit_predict(df)

        np.save(labels_path, y_labels_db)

        results(df, y_labels = y_labels_db)

    else : 
        db_scan = DBSCAN(eps = eps)
        y_labels_db = db_scan.fit_predict(df)

        results(df, y_labels = y_labels_db)


#========================= HM clustering =========================

#-----------------function to make sample of 3000 records from the original data for the hm
def sample_for_hm (df, n_samples = 3000) : 
    return df[:3000]

#----------------function to plot dendogram for the value of k
def plot_dendo(df_hm) : 
    plt.figure(figsize=(20,7))
    plt.title("Dendogram")
    sc.dendrogram(sc.linkage(df_hm, method = 'ward'))
    plt.title('Dendogram')
    plt.xlabel("sample index")
    plt.ylabel("euclidian distance")

#--------------function to plot the hm clustering
def hm_clusters(df_hm, n_clusters, labels_path = None) : 

    if labels_path is not None : 

        hm = AgglomerativeClustering(n_clusters = n_clusters, linkage = 'ward')
        y_labels_hm = hm.fit_predict(df_hm)

        np.save(labels_path, y_labels_hm)

        results(df_hm, y_labels_hm)

    else : 
        hm = AgglomerativeClustering(n_clusters = n_clusters, linkage = 'ward')
        y_labels_hm = hm.fit_predict(df_hm)

        results(df_hm, y_labels_hm)



#========================= Price column vs Train Data =========================

#-------------Function to plot the scatter plot for the price column with respect to the clusters for the comparison
def plot_price_and_labels(df_price, labels_path) : 

    labels = np.load(labels_path)
    df_price = df_price.iloc[:, 0]

    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    # --- Scatter plot (top)
    axes[0].scatter(labels, df_price, alpha=0.5)
    axes[0].set_xlabel("Cluster Label")
    axes[0].set_ylabel("Price")
    axes[0].set_title("Price distribution across clusters")

    # --- Boxplot (bottom)
    df_plot = pd.DataFrame({
        "cluster": labels,
        "price": df_price
    })

    df_plot.boxplot(column="price", by="cluster", ax=axes[1])
    axes[1].set_title("Price by Cluster")

    plt.suptitle("")   # remove pandas default title
    plt.tight_layout()
    plt.show()

