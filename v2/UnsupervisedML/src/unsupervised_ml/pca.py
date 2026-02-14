import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


#----------------function to find the correlation between the features

def get_corr(df) : 
    corr = df.corr()

    return corr

#----------------function to return the explained variance ratio
def pca_and_variance(df) : 
    pca = PCA()

    pca.fit_transform(df)

    arr = np.array(pca.explained_variance_ratio_)
    np.set_printoptions(suppress = True)

    return arr


#--------------function to reduce the dimensionality of the dataframe to 2
def reduce_dim(df) : 
    pca = PCA(n_components = 2)

    df_pca = pca.fit_transform(df)

    return df_pca


### function to check the shape
def get_shape(df) : 
    return df.shape