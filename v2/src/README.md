### Folder : SRC
- this folder contains all the resusuable functions in form of the python files, that were used in the jupyter notebook files. Further there are many subfolder inside of it, follow this file to find out more about those subfolders and individual purpose they serve.


### ----------- subfolder : data ----------------

- this folder has only one python file : (load_data.py), this file conatins 
1. load_data(file_path) : this function is used to load the particular data file, given the path of that file
2. get_shape(df) : get the shape of the dataset
3. get_nan(df) : get the null value count in the dataset
4. get_info(df) : check for the type of columns
5. save_data(df, path) : save the final data


### ---------- subfolder : featured_engineering -------------------
- one of the core folder in the entire project. it has many python files, each one with it's own uniwue purpose.


=====> file : processing_cols.py
1. unique_values(df, col) : gets the unique values present inside a particular column
2. value_counts(df, col) : gets the value count for each individual categories in a column
3. one_hot(df, col) : applies the one hot encoding to the categorical column
4. label_encoding(df, col, mapping) : applies the label encoding to the feature based on the mapping given
5. split_numerical(df, col) : splits the numerical column based on the operators(inside of the function is if-else condition)
6. split_numerical_further(df, col) : further splits the some numerical columns, that needs the more processing, even after first split
7. columns_to_drop(df, cols) : drop the columns


=====> file : plot_features.py
1. plot_graphs(df, feature) : plots hist, qq and box plot for the numerical features.
2. plot_graphs_post_scaling(df, df_copy, feature) : plots the box plots for the numerical feature of df and df_copy, after the sacler is applied on the main dataframe (df), (mainly for the distance based models)


=====> file : outliers.py (used for the distance based models mainly)
1. iqr_score(df, feature) : calculates the iq score for the feature, return the iqr score and q3 and q1 in the form of list : [Q, Q1, IQR].
2. adjust_values(df, feature, lower_limit, upper_limit) : restricts the values accordingly and remove the outliers.


=====> file : scalers.py
1. scale_feature(df, cols, scaler_path = None) : scaler the features and then save the scaler object.


### ----------- subfolder : models ------------------------------
- this folder has all the files that were used once the preprocessing part was done. has the models and prediction part in it


=====> file : split_data.py
1. data_split(df, price = None) : split the data into the train/test data or eval data, depending on the input given.


=====> file : pred_plot_trees.py
1. metrices(y_test, y_pred) : has the different metrices that compare the predicted ones to the actual ones. (called implicitly, never explicitly)

2. plot(y_test, y_pred) : plot the scatter plot and best fit line to compare the predictions. (called implicitly, never explicitly)

3. plot_and_pred_train(X_train, X_test, y_train, y_test, model, model_path) : train the model and predict on the test data, then save the model to the given path. calls the metrices() and plot() functions to compare the results to the actual one

4. best_model_pred(X_eval, best_model_path) : after finding the best model with best results from plot_and_pred_train() function, it is given the best model to predict on the eval data and then it returns those predictions that are being saved later.

5. other_model_pred(X_eval, y_pred_best, other_model_path) : other model predicts on the eval data, then results are compared with the best model predictions on the eval data


=====> file : pred_plot_distance.py
- this file is very similar to the pred_plot_trees.py file, with same function name and same sequence with the only difference being with the scaler.
1. metrices(y_test, y_pred) : has the different metrices that compare the predicted ones to the actual ones. (called implicitly, never explicitly)

2. plot(y_test, y_pred) : plot the scatter plot and best fit line to compare the predictions. (called implicitly, never explicitly)

3. plot_and_pred_train(X_train, X_test, y_train, y_test, model, model_path, scaler) : train the model and predict on the test data, then save the model to the given path. calls the metrices() and plot() functions to compare the results to the actual one, but after training and predictions the price scaler object is called to inverse scale and then the metrices() and plot() functions are being called.

4. best_model_pred(X_eval, best_model_path, scaler) : after finding the best model with best results from plot_and_pred_train() function, it is given the best model to predict on the eval data and then using the same price scaler object, inverse transformation is being used then the predictions are returned.

5. other_model_pred(X_eval, y_pred_best, other_model_path, scaler) : other model predicts on the eval data, then inverse transformation applied, then the results are compared with the best model predictions on the eval data.