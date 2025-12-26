### ------------ Folder name : Notebooks --------------------

- here is all the information about the notebooks folder, the stuff inside and how basically they are operating.
- in this folder is basically the notebooks file that were used while the data was processed or during the phases of applying the unsupervised ml logic with the datasets.
- these notebooks files have the exact process alongside giving the hint, how the operations were being carried out combined with the files in the src folder.


##### File : process_data.ipynb
- in this file conatins the code, logic and implementation of how the data went from intermidiate to the model ready, obvisouly, you can refer to the exact file to find the more information about it, the comments are out there in the file, you can also refer to the flowchart for the project to get the hint, as it is not possible to put the exact line by line logic here, but still I am adding the flow of the file which explains the enough to know about the file.

- flow : 
- loading the functions --> then scaled train data (with setting up paths) --> performed initial checks --> separated the price coloumn --> dropped the price feature then from the original data --> then loaded the test data --> performed inital checks(only check nan in that case) --> then setup the paths to save them at different locations --> saved the data in the model ready under the scaled.

- the above workflow was exceuted the exact same way for the non scaled data (which is tree based data technically).


##### ********************File : scaled_clustering.ipynb*****************

- in this file, we have the code/logic for how after the processing of the data, we performed the functions/methods on the scaled data (including train, test and price) to finally made the clusters in the end eventually. please refer to the exact file (named as : scaled_clutsering.ipynb in the 'notebooks' folder, currently you are in the 'docs' folder) to find more information about the code or the flowchart to get the hint of the analogy behind the process. 

- flow : 
1. Loaded the functions from the src file, setup the path for the sys and autoreloader as well -->
2. setup the path for the train, test and price (scaled data) -- >

=========== Train data ===================

3. loaded the train -->
4. performed initial checks (nan, get_shape) --> 
5. found out the correlation between the features -->
6. made the copy -->
7. use the pca and find out the covariance explained ratio on the copy data of the train -->
8. reduced the original train to 2 dimensons using the pca -->
9. again calculated the covariance ratio of the reduced data -- >
10. calculated the value of k for the kmeans clustering using wcss and elbow curve -->
11. setup the path to save the labels, use the value of k and plot the clusters --> 
12. calculated the value of eps for the db_scan clustering using the distance curve plot -->
13. setup the path to save the labels, use the value of eps and plot the clusters -->
14. reduce the size to 3000 in the new df_hm subset of the train data after pca
15. calculated the value of n_clusters for the hm clustering using dendogram -->
16. setup the path to save the labels, use the value of n_clusters and plot the clusters --> 

============ Test data ======================

- the test data already had 2.6k rows, so no reduction was done
- additionally the labels path were not setup, because the comparison with respect to the price column was not carried out, as earlier during the supervised ml phase, there was no original data at all.

17. loaded the test -->
18. performed initial checks (nan, get_shape) --> 
19. found out the correlation between the features -->
20. made the copy -->
21. use the pca and find out the covariance explained ratio on the copy data of the test -->
22. reduced the original train to 2 dimensons using the pca -->
23. again calculated the covariance ratio of the reduced data -- >
24. calculated the value of k for the kmeans clustering using the wcss score and elbow curve -->
25. use the value of k and plot the clusters --> 
26. calculated the value of eps for the db_scan clustering using the distance plot curve -->
27. use the value of eps and plot the clusters -->
28. calculated the value of n_clusters for the hm clustering using dendogram -->
29. use the value of n_clusters and plot the clusters --> 


============ Pirce data ====================
- the comparison was solely carried out against the train data, the labels path were reused to load them again from the clustering phase
- like the reduction of the rows from 10k to 3k during the hm clustering, the price dataframe was also reduced from the 10k to 3k to keep the alignment.

30. loaded the price data -->
31. just checked the df.head(), df.shape() -->
32. plot the boxplot and the scatter for the price vs the kmeans_labels saved during the clustering on the train phase -->
33. plot the boxplot and the scatter for the price vs the db_labels saved during the clustering on the train phase -->
34. reduce the size of price from 10k to 3k for the hm clustering to avoid the shape mismatching -->
35. plot the boxplot and the scatter for the price vs the hm_labels saved during the clustering on the train phase.


##### ********************File : non_scaled_clustering.ipynb*************************

- in this file, we have the code/logic for how after the processing of the data, we performed the functions/methods on the non_scaled data (including train, test and price) to finally made the clusters in the end eventually. please refer to the exact file (named as : scaled_clutsering.ipynb in the 'notebooks' folder, currently you are in the 'docs' folder) to find more information about the code or the flowchart to get the hint of the analogy behind the process. 
- this file is identical and was copy pasted using the scaled_clustering file, only the paths were modified because the pipeline that they followed was the exact same pipeline with no practical differences in them.

- flow : 
1. Loaded the functions from the src file, setup the path for the sys and autoreloader as well -->
2. setup the path for the train, test and price (non_scaled data) -- >

=========== Train data ===================

3. loaded the train -->
4. performed initial checks (nan, get_shape) --> 
5. found out the correlation between the features -->
6. made the copy -->
7. use the pca and find out the covariance explained ratio on the copy data of the train -->
8. reduced the original train to 2 dimensons using the pca -->
9. again calculated the covariance ratio of the reduced data -- >
10. calculated the value of k for the kmeans clustering using wcss and elbow curve -->
11. setup the path to save the labels, use the value of k and plot the clusters --> 
12. calculated the value of eps for the db_scan clustering using the distance curve plot -->
13. setup the path to save the labels, use the value of eps and plot the clusters -->
14. reduce the size to 3000 in the new df_hm subset of the train data after pca
15. calculated the value of n_clusters for the hm clustering using dendogram -->
16. setup the path to save the labels, use the value of n_clusters and plot the clusters --> 

============ Test data ======================

- the test data already had 2.6k rows, so no reduction was done
- additionally the labels path were not setup, because the comparison with respect to the price column was not carried out, as earlier during the supervised ml phase, there was no original data at all.

17. loaded the test -->
18. performed initial checks (nan, get_shape) --> 
19. found out the correlation between the features -->
20. made the copy -->
21. use the pca and find out the covariance explained ratio on the copy data of the test -->
22. reduced the original train to 2 dimensons using the pca -->
23. again calculated the covariance ratio of the reduced data -- >
24. calculated the value of k for the kmeans clustering using the wcss score and elbow curve -->
25. use the value of k and plot the clusters --> 
26. calculated the value of eps for the db_scan clustering using the distance plot curve -->
27. use the value of eps and plot the clusters -->
28. calculated the value of n_clusters for the hm clustering using dendogram -->
29. use the value of n_clusters and plot the clusters --> 


============ Pirce data ====================
- the comparison was solely carried out against the train data, the labels path were reused to load them again from the clustering phase
- like the reduction of the rows from 10k to 3k during the hm clustering, the price dataframe was also reduced from the 10k to 3k to keep the alignment.

30. loaded the price data -->
31. just checked the df.head(), df.shape() -->
32. plot the boxplot and the scatter for the price vs the kmeans_labels saved during the clustering on the train phase -->
33. plot the boxplot and the scatter for the price vs the db_labels saved during the clustering on the train phase -->
34. reduce the size of price from 10k to 3k for the hm clustering to avoid the shape mismatching -->
35. plot the boxplot and the scatter for the price vs the hm_labels saved during the clustering on the train phase.