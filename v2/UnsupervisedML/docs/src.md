### ------------ Folder name : src --------------------

- here is all the information about the src folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- src folder is the one containing the python code mostly in form of function that was later reused again and again in the notebook files, before completing the report part.

- this folder structure is bit more complex with many subfolders inside and functions inside of the files in those subfolders, but here I try to give the best explanantion I could give, to guide you through the folder.

- further this folder is divided into the 2* subfolders : 1. process_data, 2. unsupervised_ml
- (*)sign after the (2) in the above statment means that at the time of documentation we only have 2 folders, but for sure there are gonna be more as the project proceed ahead. to find out more you can always refer to the github to track those changes and what exactly was there.


##### Subfolder : process_data
- in this folder we have the src files that were being used to perform the basic processing actions of the data to convert it from intermidiate form to the model ready form, additionally it also has (__init__.py) file to export out those functions to be called in the notebooks.
- these functions from the src files were used in with the combination of notebook files (process_data.ipynb) only.
- in this particular subfolder we have only one (data.py) file with all functions inside it.

====> (file : data.py)
- this file has the following content : 
1. load_data(df_path) : loads the dataframe based on the path given to it
2. get_nan(df) : return the nan values in the dataset
3. get_info(df) : gives the info(the data type of the columns) of the dataset/dataframe
4. drop_col(df, col) : drop the column/columns from the dataset (along the vertical axis i.e. axis = 1)
5. save_data(df, path) : save the data to the particular location on the basis of the location(path) given to it
6. get_shape(df) : return the shape of the dataset



##### Subfolder : unsupervised_ml
- in this folder we have the src files that were used inside and in combination with the (scaled_clustering.ipynb, non_scaled_clustering.ipynb) files. the functions are responsible for the further work on the model ready data which includes (but not limited to) reducing the dimensionality using the pca, veryfying the co variance using the pca, applying the different clustering models and saving those labels for the later stages to verify the clusters with the price feature.
- in this folder we have (__init__.py) file responsible to make the export of those functions possible, (clustering.py) and (pca.py) files.

====> (file : pca.py)
- this file contains : 
1. get_corr(df) : gives the correlation between the different features of the dataset
2. pca_and_variance(df) : fit the pca on the data frame without reducing the dimensionality and then gives the variance ratio to study the differences in different features
3. reduce_dim(df) : reduces the dimensons of the dataset by using the pca (set to 2 for the dataset)

====> (file : clustering.py)
- this file contains : 
1. results(df, y_labels) : gives the silhouette score, plot the scatter plot based on the clusters (never called explicitlu, used internally inside the other functions only)

2. find_k(df) : find the value of the k for the kmeans clustering, using the wcss score and the elbow curve

3. kmeans_clutsers(df, k, labels_path = None) : plots the kmeans clusters based on the value of the k, that we got from the above function, it also saved the labels based on the path given to it (**only incase of the train data for both scaled and non_scaled, we saved the labels and gave the bath to compare with the original price data, meanwhile, for the test data there was no actual price column that exsisted**).

4. find_eps(df) : find the value of eps for the dbscan clustering by plotting the distance curve plot.

5. db_clusters(df, eps, labels_path = None) : plots the dbscan clusters based on the value of the eps, that we got from the above function, it also saved the labels based on the path given to it

6. sample_for_hm (df, n_samples = 3000) : reduce the size of the dataset to 3k rows(**was used for the hm clustering because of the lack of hardware support**)

7. plot_dendo(df_hm) : plots the dendogram to find the value of n_clusters to use the Agglomerative clustering

8. hm_clusters(df_hm, n_clusters, labels_path = None) : plots the hm clusters based on the value of the n_clusters, that we got from the above function, it also saved the labels based on the path given to it

9. plot_price_and_labels(df_price, labels_path) : plots the scatter plot and box plot for the original price data with respect to the different labels from above functions that were saved later
- (**for the hm, the size for the both train dataset and the price data was down from 10k to 3k**)